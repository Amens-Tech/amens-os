class PromptBuilder:

    @staticmethod
    def build(event, project):

        if event.actor == "sofiane":
            return f"""
You are the CTO of Amens Tech.

Project:
{project}

Your task:
Launch the project, explain the objective to the team, define the first milestones and assign the work to Ibrahim.

Answer in French.
""".strip()

        if event.actor == "ibrahim":
            return f"""
You are the lead Python developer of Amens Tech.

Project:
{project}

Task:
{event.description}

Work only inside your workspace.
Use Git when appropriate.
Answer in French with:
- what you did
- next steps
""".strip()

        return event.description
