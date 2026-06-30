from pathlib import Path


class LLM:

    def __init__(self, prompts_dir="prompts"):
        self.prompts_dir = Path(prompts_dir)

    def load_prompt(self, actor):
        with open(self.prompts_dir / f"{actor}.md", "r") as f:
            return f.read()

    def generate(self, actor, instruction):

        prompt = self.load_prompt(actor)

        return {
            "actor": actor,
            "system_prompt": prompt,
            "instruction": instruction,
        }
