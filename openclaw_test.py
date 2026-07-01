from connectors.openclaw import OpenClawConnector

client = OpenClawConnector()

reply = client.ask(
    agent="ibrahim",
    session_key="project:windows-evtx-parser",
    message="Quel est le langage du projet ? Réponds en une ligne.",
)

print(reply)
