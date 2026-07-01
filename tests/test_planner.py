import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.services.planner import Planner
from core.models.event import EventType


def test_planner_first_project(tmp_path):
    state_file = tmp_path / "state.json"
    state_file.write_text(json.dumps({
        "current_project": None,
        "phase": "idle",
        "current_story": None,
        "employees": {
            "sofiane": {"status": "idle"},
            "product-manager": {"status": "idle"},
            "ibrahim": {"status": "idle"},
            "qa": {"status": "idle"}
        }
    }))

    planner = Planner(state_file=state_file)
    event = planner.next_action()

    assert event.event_type == EventType.SLACK_MESSAGE
    assert event.actor == "sofiane"


def test_state_updated(tmp_path):
    state_file = tmp_path / "state.json"
    state_file.write_text(json.dumps({
        "current_project": None,
        "phase": "idle",
        "current_story": None,
        "employees": {
            "sofiane": {"status": "idle"},
            "product-manager": {"status": "idle"},
            "ibrahim": {"status": "idle"},
            "qa": {"status": "idle"}
        }
    }))

    planner = Planner(state_file=state_file)
    planner.next_action()

    state = planner.load_state()

    assert state["current_project"] is not None
