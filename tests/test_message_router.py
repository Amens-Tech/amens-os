from core.services.message_router import MessageRouter


def test_parse():

    reply = """
{
    "status":"COMPLETED",
    "to":"ibrahim",
    "phase":"development",
    "slack_message":"Bonjour Ibrahim",
    "next_action":"Créer la CLI"
}
"""

    msg = MessageRouter.parse(reply)

    assert msg.status == "COMPLETED"
    assert msg.to == "ibrahim"
    assert msg.phase == "development"
    assert msg.slack_message == "Bonjour Ibrahim"
    assert msg.next_action == "Créer la CLI"
