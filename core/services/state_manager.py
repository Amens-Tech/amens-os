import json


class StateManager:

    def __init__(self, path="state/state.json"):
        self.path = path

    def load(self):
        with open(self.path, "r") as f:
            return json.load(f)
