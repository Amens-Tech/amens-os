from connectors.openclaw import OpenClawConnector


class DevelopmentService:

    def __init__(self):
        self.agent = OpenClawConnector()

    def work(self, project, actor, task):

        return self.agent.ask(
            agent=actor,
            session_key=f"project:{project}",
            message=task,
        )
