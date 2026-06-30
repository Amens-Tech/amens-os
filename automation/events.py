from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class EventType(Enum):
    SLACK_MESSAGE = "slack_message"
    GIT_COMMIT = "git_commit"
    GIT_PUSH = "git_push"
    WAIT = "wait"


@dataclass
class Event:
    event_type: EventType
    actor: str
    description: str
    created_at: datetime

    def __str__(self):
        return f"[{self.created_at}] {self.actor}: {self.event_type.value} -> {self.description}"
