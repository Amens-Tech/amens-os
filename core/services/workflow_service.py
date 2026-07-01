class WorkflowService:

    TRANSITIONS = {
        "planning": "backlog",
        "backlog": "development",
        "development": "testing",
        "testing": "review",
        "review": "idle",
    }

    @classmethod
    def advance(cls, state):
        phase = state["phase"]

        if phase not in cls.TRANSITIONS:
            return state

        next_phase = cls.TRANSITIONS[phase]

        state["phase"] = next_phase

        if next_phase == "idle":
            state["current_project"] = None
            state["current_story"] = None

        return state
