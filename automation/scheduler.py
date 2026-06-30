from datetime import datetime
from zoneinfo import ZoneInfo
import random
import yaml

from automation.events import Event, EventType


class Scheduler:

    def __init__(self, config_path="config/scheduler.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

    def _now(self, timezone):
        return datetime.now(ZoneInfo(timezone))

    def is_working_day(self):
        now = self._now("Europe/Brussels")
        return now.strftime("%A").lower() in self.config["working_days"]

    def is_employee_working(self, employee):

        if not self.is_working_day():
            return False

        cfg = self.config["working_hours"][employee]

        now = self._now(cfg["timezone"]).time()

        start = datetime.strptime(cfg["start"], "%H:%M").time()
        end = datetime.strptime(cfg["end"], "%H:%M").time()

        return start <= now <= end

    def company_is_open(self):
        return (
            self.is_employee_working("sofiane")
            or self.is_employee_working("ibrahim")
        )

    def next_event(self):

        if not self.company_is_open():
            return Event(
                EventType.WAIT,
                "system",
                "Company closed",
                datetime.now(),
            )

        events = [
            (
                EventType.SLACK_MESSAGE,
                "sofiane",
                "Discuss current project",
            ),
            (
                EventType.GIT_COMMIT,
                "ibrahim",
                "Commit Python changes",
            ),
            (
                EventType.GIT_PUSH,
                "ibrahim",
                "Push latest commits",
            ),
        ]

        event = random.choice(events)

        return Event(
            event_type=event[0],
            actor=event[1],
            description=event[2],
            created_at=datetime.now(),
        )
