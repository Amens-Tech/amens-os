import subprocess


class GitHubConnector:

    def git(self, *args):
        result = subprocess.run(
            ["git", *args],
            capture_output=True,
            text=True,
        )
        return result.stdout.strip(), result.stderr.strip()

    def status(self):
        return self.git("status")

    def add_all(self):
        return self.git("add", ".")

    def commit(self, message):
        return self.git("commit", "-m", message)
