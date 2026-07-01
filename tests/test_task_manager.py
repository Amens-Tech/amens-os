import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.repositories.task_repository import TaskManager


def test_next_task():

    manager = TaskManager()

    task = manager.next_task()

    assert task is not None
    assert task.status == "todo"
