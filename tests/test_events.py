import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.models.event import Event, EventType


def test_event_creation():
    event = Event(
        event_type=EventType.SLACK_MESSAGE,
        actor="sofiane",
        description="Start new project",
        created_at=datetime.now(),
    )

    assert event.actor == "sofiane"
    assert event.event_type == EventType.SLACK_MESSAGE
