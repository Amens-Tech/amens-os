import json
from pathlib import Path
from datetime import datetime

from core.models.event import Event, EventType


class Planner:

    PHASE_ACTORS = {
        "planning": ("sofiane", "Plan project"),
        "backlog": ("product-manager", "Create backlog for"),
        "development": ("ibrahim", "Develop"),
        "testing": ("qa", "Test"),
        "review": ("sofiane", "Review"),
    }

    def __init__(
        self,
        state_file="state/state.json",
        backlog_file="backlog/projects.json",
    ):
        self.state_file = Path(state_file)
        self.backlog_file = Path(backlog_file)

    def load_state(self):
        return json.loads(self.state_file.read_text())

    def save_state(self, state):
        self.state_file.write_text(json.dumps(state, indent=2))

    def load_backlog(self):
        return json.loads(self.backlog_file.read_text())

    def next_action(self):

        state = self.load_state()

        if state["phase"] == "idle":

            backlog = self.load_backlog()

            project = next(
                p for p in backlog
                if p["status"] == "todo"
            )

            state["current_project"] = project["name"]
            state["phase"] = "planning"

            self.save_state(state)

        phase = state["phase"]

        if phase not in self.PHASE_ACTORS:
            return None

        actor, action = self.PHASE_ACTORS[phase]

        return Event(
            event_type=EventType.SLACK_MESSAGE,
            actor=actor,
            description=f"{action} {state['current_project']}",
            created_at=datetime.now(),
        )
