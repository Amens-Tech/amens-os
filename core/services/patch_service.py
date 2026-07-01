import re
import subprocess
import tempfile


class PatchService:

    @staticmethod
    def extract(reply):

        m = re.search(
            r"```diff(.*?)```",
            reply,
            re.DOTALL,
        )

        if not m:
            return None

        return m.group(1).strip()

    @staticmethod
    def apply(diff):

        if diff is None:
            return False

        with tempfile.NamedTemporaryFile(
            suffix=".patch",
            mode="w",
            delete=False,
        ) as f:

            f.write(diff)
            patch = f.name

        result = subprocess.run(
            ["git", "apply", patch],
            capture_output=True,
            text=True,
        )

        return result.returncode == 0

    @staticmethod
    def rollback():

        subprocess.run(
            ["git", "restore", "."]
        )
