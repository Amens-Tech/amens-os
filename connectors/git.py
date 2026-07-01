import subprocess


class GitConnector:

    def status(self):
        return subprocess.run(
            ["git", "status", "--short"],
            capture_output=True,
            text=True,
        ).stdout.strip()

    def add_all(self):
        subprocess.run(["git", "add", "."], check=True)

    def commit(self, message):
        subprocess.run(
            ["git", "commit", "-m", message],
            check=True,
        )

    def push(self):
        subprocess.run(
            [
                "git",
                "push",
            ],
            check=True,
        )
