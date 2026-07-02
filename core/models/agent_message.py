from dataclasses import dataclass


@dataclass
class AgentMessage:
    status: str
    to: str
    phase: str
    slack_message: str
    next_action: str | None = None
