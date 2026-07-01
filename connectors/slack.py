import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackConnector:

    def __init__(self):
        token = os.getenv("SLACK_BOT_TOKEN")
        self.client = WebClient(token=token) if token else None

    def send_message(self, channel, text):

        if self.client is None:
            print(f"[SLACK disabled] #{channel}")
            print(text)
            return None

        try:
            response = self.client.chat_postMessage(
                channel=channel,
                text=text,
            )

            return response["ts"]

        except SlackApiError as e:
            print(e.response["error"])
            return None
