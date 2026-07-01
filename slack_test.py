from dotenv import load_dotenv

load_dotenv()

from connectors.slack import SlackConnector

slack = SlackConnector()

slack.send_message(
    "amens-dev",
    "🚀 Premier message envoyé par Amens OS"
)

print("Done")
