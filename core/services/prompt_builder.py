from pathlib import Path


class PromptBuilder:

    PROMPTS = Path("prompts")

    @classmethod
    def build(cls, event, project):

        template = (
            cls.PROMPTS / f"{event.actor}.md"
        ).read_text()

        return (
            template
            .replace("{{PROJECT}}", project)
            .replace("{{TASK}}", event.description)
        )
