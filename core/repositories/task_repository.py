import json
from pathlib import Path

from core.models.task import Task


class TaskManager:

    def __init__(self, file="backlog/tasks.json"):
        self.file = Path(file)

    def _load(self):
        return json.loads(self.file.read_text())

    def _save(self, data):
        self.file.write_text(json.dumps(data, indent=2))

    def all(self):
        return [Task(**t) for t in self._load()]

    def next_task(self):

        for task in self.all():
            if task.status == "todo":
                return task

        return None

    def update_status(self, task_id, status):

        data = self._load()

        for task in data:
            if task["id"] == task_id:
                task["status"] = status

        self._save(data)
