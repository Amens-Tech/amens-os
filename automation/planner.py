import json
from pathlib import Path

from automation.events import Event, EventType
from datetime import datetime


class Planner:

    def __init__(self, state_file="state/state.json"):
        self.state_file = Path(state_file)

    def load_state(self):
        with open(self.state_file, "r") as f:
            return json.load(f)

    def next_action(self):

        state = self.load_state()

        if state["current_project"] is None:
            return Event(
                event_type=EventType.SLACK_MESSAGE,
                actor="sofiane",
                description="Launch a new cybersecurity project",
                created_at=datetime.now(),
            )

        return Event(
            event_type=EventType.WAIT,
            actor="system",
            description="No action required",
            created_at=datetime.now(),
        )
