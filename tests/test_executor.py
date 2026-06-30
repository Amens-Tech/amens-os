import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from automation.executor import Executor
from automation.events import Event, EventType


def test_execute_slack_message():
    event = Event(
        event_type=EventType.SLACK_MESSAGE,
        actor="sofiane",
        description="Launch project",
        created_at=datetime.now(),
    )

    executor = Executor()
    result = executor.execute(event)

    assert result["status"] == "executed"
    assert result["action"] == "send_slack_message"
    assert result["actor"] == "sofiane"
