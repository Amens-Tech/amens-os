import subprocess


class VerificationService:

    @staticmethod
    def pytest():

        result = subprocess.run(
            ["pytest", "-q"],
            capture_output=True,
            text=True,
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }

    @staticmethod
    def git_status():

        result = subprocess.run(
            ["git", "status", "--short"],
            capture_output=True,
            text=True,
        )

        return result.stdout.strip()

    @staticmethod
    def last_commit():

        result = subprocess.run(
            ["git", "log", "-1", "--oneline"],
            capture_output=True,
            text=True,
        )

        return result.stdout.strip()
