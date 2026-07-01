import os

from connectors.slack import SlackConnector
from automation.events import EventType
from automation.llm import LLM


class Executor:

    def __init__(self):
        self.slack = SlackConnector()
        self.llm = LLM()

    def execute(self, event):

        if event.event_type == EventType.WAIT:
            return

        if event.event_type == EventType.SLACK_MESSAGE:
            message = self.llm.generate_message(
                actor=event.actor,
                instruction=event.description,
            )

            self.slack.send_message(
                os.environ["SLACK_CHANNEL_NAME"],
                message,
            )

            return

        if event.event_type == EventType.GIT_COMMIT:
            print(f"[GIT] {event.description}")
            return

        if event.event_type == EventType.GIT_PUSH:
            print(f"[PUSH] {event.description}")
            return
