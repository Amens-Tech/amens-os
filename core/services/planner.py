import json
from pathlib import Path
from datetime import datetime

from core.models.event import Event, EventType


class Planner:

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

            return Event(
                event_type=EventType.SLACK_MESSAGE,
                actor="sofiane",
                description=f"Plan project {project['name']}",
                created_at=datetime.now(),
            )

        if state["phase"] == "planning":

            state["phase"] = "backlog"

            self.save_state(state)

            return Event(
                event_type=EventType.SLACK_MESSAGE,
                actor="product-manager",
                description=f"Create backlog for {state['current_project']}",
                created_at=datetime.now(),
            )

        if state["phase"] == "backlog":

            state["phase"] = "development"

            self.save_state(state)

            return Event(
                event_type=EventType.SLACK_MESSAGE,
                actor="ibrahim",
                description=f"Develop {state['current_project']}",
                created_at=datetime.now(),
            )

        if state["phase"] == "development":

            state["phase"] = "testing"

            self.save_state(state)

            return Event(
                event_type=EventType.SLACK_MESSAGE,
                actor="qa",
                description=f"Test {state['current_project']}",
                created_at=datetime.now(),
            )

        if state["phase"] == "testing":

            state["phase"] = "review"

            self.save_state(state)

            return Event(
                event_type=EventType.SLACK_MESSAGE,
                actor="sofiane",
                description=f"Review {state['current_project']}",
                created_at=datetime.now(),
            )

        state["phase"] = "idle"
        state["current_project"] = None

        self.save_state(state)

        return None
