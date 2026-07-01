from pathlib import Path


class LLM:

    def __init__(self, prompts_dir="prompts"):
        self.prompts_dir = Path(prompts_dir)

    def load_prompt(self, actor):
        with open(self.prompts_dir / f"{actor}.md", "r") as f:
            return f.read()

    def generate_message(self, actor, instruction):
        prompt = self.load_prompt(actor)

        if actor == "sofiane":
            return (
                "Salut Ibrahim. On a besoin de lancer un outil Python interne "
                "pour le projet windows-evtx-parser. L'objectif est d'accélérer "
                "l'analyse des journaux Windows sur nos missions DFIR/SOC. "
                "Commence par une base simple, propre et testable. Tu me fais "
                "un premier retour quand tu as quelque chose qui tourne."
            )

        if actor == "ibrahim":
            return (
                "Salut Sofiane, ok je regarde ça mnt 👍. Je vais commencer par "
                "structurer le projet Python et voir comment parser proprement "
                "les fichiers EVTX. Je te redis dès que j'ai une première base."
            )

        return instruction
