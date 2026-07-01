import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.models.task import Task


def test_task_creation():

    task = Task(
        id=1,
        project="windows-evtx-parser",
        title="Implement parser",
        description="Create parser",
        assignee="ibrahim",
        priority="high",
        status="todo",
    )

    assert task.assignee == "ibrahim"
    assert task.status == "todo"
