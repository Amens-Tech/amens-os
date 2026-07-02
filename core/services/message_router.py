import json
import re

from core.models.agent_message import AgentMessage


class MessageRouter:

    @staticmethod
    def parse(reply: str) -> AgentMessage:

        # New JSON protocol
        match = re.search(r"\{.*\}", reply, re.DOTALL)

        if match:
            try:
                data = json.loads(match.group(0))
                return AgentMessage(
                    status=data.get("status", "UNKNOWN"),
                    to=data.get("to", ""),
                    phase=data.get("phase", ""),
                    slack_message=data.get("slack_message", ""),
                    next_action=data.get("next_action"),
                )
            except json.JSONDecodeError:
                pass

        # Legacy fallback: STATUS + text/diff
        status_match = re.search(r"STATUS:\s*(\w+)", reply)
        status = status_match.group(1) if status_match else "UNKNOWN"

        cleaned = re.sub(r"\[agent\].*", "", reply, flags=re.DOTALL).strip()
        cleaned = re.sub(r"STATUS:\s*\w+", "", cleaned).strip()

        return AgentMessage(
            status=status,
            to="qa",
            phase="testing",
            slack_message=cleaned or "J'ai terminé ma partie et je propose de passer à la validation.",
            next_action="Validation QA",
        )
