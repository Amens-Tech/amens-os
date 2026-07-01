import subprocess


class GitService:

    def run(self, *args):
        result = subprocess.run(
            ["git", *args],
            capture_output=True,
            text=True,
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }

    def status(self):
        return self.run("status")

    def add(self):
        return self.run("add", ".")

    def commit(self, message):
        return self.run("commit", "-m", message)

    def push(self):
        return self.run("push")
