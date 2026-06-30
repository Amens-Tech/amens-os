from automation.events import EventType


class Executor:

    def execute(self, event):

        if event.event_type == EventType.WAIT:
            return {
                "status": "skipped",
                "reason": event.description,
            }

        if event.event_type == EventType.SLACK_MESSAGE:
            return {
                "status": "executed",
                "action": "send_slack_message",
                "actor": event.actor,
                "message": event.description,
            }

        if event.event_type == EventType.GIT_COMMIT:
            return {
                "status": "executed",
                "action": "git_commit",
                "actor": event.actor,
                "message": event.description,
            }

        if event.event_type == EventType.GIT_PUSH:
            return {
                "status": "executed",
                "action": "git_push",
                "actor": event.actor,
                "message": event.description,
            }

        return {
            "status": "error",
            "reason": "Unknown event type",
        }
