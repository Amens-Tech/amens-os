from connectors.openclaw import OpenClawConnector
from core.services.state_manager import StateManager
from core.services.prompt_builder import PromptBuilder
from core.services.artifact_service import ArtifactService
from core.services.status_parser import StatusParser
from core.services.workflow_service import WorkflowService
from core.services.patch_service import PatchService
from core.services.verification_service import VerificationService
from connectors.slack import SlackConnector
from core.models.event import EventType


class Executor:

    def __init__(self):
        self.openclaw = OpenClawConnector()
        self.slack = SlackConnector()
        self.state = StateManager().load()

    def execute(self, event):

        if event.event_type == EventType.WAIT:
            return

        if event.event_type == EventType.SLACK_MESSAGE:

            reply = self.openclaw.ask(
                agent=event.actor,
                session_key=f"project:{self.state['current_project']}",
                message=PromptBuilder.build(
                    event,
                    self.state["current_project"],
                ),
            )

            status = StatusParser.parse(reply)

            print(f"[STATUS] {status}")

            if status == "COMPLETED" and event.actor == "ibrahim":
                diff = PatchService.extract(reply)

                if diff:
                    print("[PATCH] found")

                    if not PatchService.apply(diff):
                        print("[PATCH] apply failed")
                        PatchService.rollback()
                        status = "BLOCKED"
                    else:
                        print("[PATCH] applied")

                        verification = VerificationService.pytest()

                        if verification["success"]:
                            print("[VERIFY] pytest OK")
                            self.state = WorkflowService.advance(self.state)
                            StateManager().save(self.state)
                            print(f"[PHASE] -> {self.state['phase']}")
                        else:
                            print("[VERIFY] pytest FAILED")
                            print(verification["stdout"])
                            print(verification["stderr"])
                            PatchService.rollback()
                            status = "BLOCKED"

                else:
                    print("[PATCH] no diff found")
                    status = "BLOCKED"

            elif status == "COMPLETED":
                self.state = WorkflowService.advance(self.state)
                StateManager().save(self.state)
                print(f"[PHASE] -> {self.state['phase']}")

            artifact_map = {
                "sofiane": "vision" if self.state.get("phase") == "planning" else "review",
                "product-manager": "backlog",
                "ibrahim": "development",
                "qa": "qa",
            }

            artifact_name = artifact_map.get(event.actor)

            if artifact_name and self.state.get("current_project"):
                ArtifactService(
                    self.state["current_project"]
                ).write(
                    artifact_name,
                    reply,
                )

            self.slack.send_message(
                "amens-dev",
                reply,
            )

            return

        if event.event_type == EventType.GIT_COMMIT:
            print(f"[GIT] {event.description}")
