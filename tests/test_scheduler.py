import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from automation.scheduler import Scheduler


def test_scheduler_loads():
    scheduler = Scheduler()
    assert scheduler.config is not None


def test_working_day():
    scheduler = Scheduler()
    assert isinstance(scheduler.is_working_day(), bool)
