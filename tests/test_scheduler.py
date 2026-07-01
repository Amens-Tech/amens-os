import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.services.scheduler import Scheduler


def test_scheduler_loads():
    scheduler = Scheduler()
    assert scheduler.config is not None


def test_working_day():
    scheduler = Scheduler()
    assert isinstance(scheduler.is_working_day(), bool)


def test_company_open():
    scheduler = Scheduler()
    assert isinstance(scheduler.company_is_open(), bool)


def test_sofiane():
    scheduler = Scheduler()
    assert isinstance(scheduler.is_employee_working("sofiane"), bool)


def test_ibrahim():
    scheduler = Scheduler()
    assert isinstance(scheduler.is_employee_working("ibrahim"), bool)

def test_next_event():
    scheduler = Scheduler()
    event = scheduler.next_event()
    assert event is not None
