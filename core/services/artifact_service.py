from pathlib import Path


class ArtifactService:

    def __init__(self, project):
        self.root = Path(f"projects/{project}/docs")
        self.root.mkdir(parents=True, exist_ok=True)

    def write(self, name, content):
        path = self.root / f"{name}.md"
        path.write_text(content)

    def read(self, name):
        path = self.root / f"{name}.md"
        if path.exists():
            return path.read_text()
        return ""
