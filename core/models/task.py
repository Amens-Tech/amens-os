from dataclasses import dataclass


@dataclass
class Task:
    id: int
    project: str
    title: str
    description: str
    assignee: str
    priority: str
    status: str
