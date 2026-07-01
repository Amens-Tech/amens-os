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
        with open(self.state_file) as f:
            return json.load(f)

    def save_state(self, state):
        with open(self.state_file, "w") as f:
            json.dump(state, f, indent=2)

    def load_backlog(self):
        with open(self.backlog_file) as f:
            return json.load(f)

    def next_action(self):

        state = self.load_state()

        if state["current_project"] is None:

            backlog = self.load_backlog()

            project = next(
                p for p in backlog if p["status"] == "todo"
            )

            state["current_project"] = project["name"]
            state["employees"]["sofiane"]["status"] = "planning"
            state["employees"]["ibrahim"]["status"] = "waiting"

            self.save_state(state)

            return Event(
                event_type=EventType.SLACK_MESSAGE,
                actor="sofiane",
                description=f"Launch project: {project['name']}",
                created_at=datetime.now(),
            )

        if state["employees"]["ibrahim"]["status"] == "waiting":

            state["employees"]["ibrahim"]["status"] = "working"

            self.save_state(state)

            return Event(
                event_type=EventType.SLACK_MESSAGE,
                actor="ibrahim",
                description="I'll start working on it.",
                created_at=datetime.now(),
            )

        return Event(
            event_type=EventType.GIT_COMMIT,
            actor="ibrahim",
            description="Continue Python development",
            created_at=datetime.now(),
        )
