import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from automation.planner import Planner
from automation.events import EventType


def test_planner_first_project():
    planner = Planner()
    event = planner.next_action()

    assert event.event_type == EventType.SLACK_MESSAGE
    assert event.actor == "sofiane"
