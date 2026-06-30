from datetime import datetime
from zoneinfo import ZoneInfo
import yaml


class Scheduler:

    def __init__(self, config_path="config/scheduler.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

    def is_working_day(self):
        today = datetime.now().strftime("%A").lower()
        return today in self.config["working_days"]

    def company_is_open(self):
        return self.is_working_day()
