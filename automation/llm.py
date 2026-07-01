from pathlib import Path


class LLM:

    def __init__(self):
        self.templates = Path("templates")
        self.prompts = Path("prompts")

    def load_prompt(self, actor):
        return (self.prompts / f"{actor}.md").read_text()

    def generate_message(self, actor, event=None, instruction=None):

        if actor == "sofiane":

            text = (self.templates / "sofiane_project.txt").read_text()

            return (
                text.replace("{{project}}", "windows-evtx-parser")
                    .replace(
                        "{{objective}}",
                        "Créer un parser Windows EVTX réutilisable."
                    )
                    .replace("{{priority}}", "Haute")
            )

        if actor == "ibrahim":
            return (self.templates / "ibrahim_ack.txt").read_text()

        if instruction:
            return instruction

        if event:
            return event.description

        return ""
