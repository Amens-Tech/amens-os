import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackConnector:

    def __init__(self):
        self.client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

    def send_message(self, channel, text):

        try:
            response = self.client.chat_postMessage(
                channel=channel,
                text=text,
            )

            return response["ts"]

        except SlackApiError as e:
            print(e.response["error"])
            return None
