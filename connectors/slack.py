import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackConnector:

    def __init__(self):
        token = os.getenv("SLACK_BOT_TOKEN")
        self.client = WebClient(token=token) if token else None

    def send_message(self, channel, text, thread_ts=None):

        if self.client is None:
            print(f"[SLACK disabled] #{channel}")
            if thread_ts:
                print(f"[THREAD] {thread_ts}")
            print(text)
            return None

        try:
            response = self.client.chat_postMessage(
                channel=channel,
                text=text,
                thread_ts=thread_ts,
            )
            return response["ts"]

        except SlackApiError as e:
            print(e.response["error"])
            return None
