import json


class StateManager:

    def __init__(self, path="state/state.json"):
        self.path = path

    def load(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def save(self, state):
        with open(self.path, "w") as f:
            json.dump(state, f, indent=2)
