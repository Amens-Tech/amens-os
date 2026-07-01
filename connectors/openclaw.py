import subprocess


class OpenClawConnector:

    def ask(self, agent, message, session_key=None):
        cmd = [
            "openclaw",
            "agent",
            "--agent",
            agent,
            "--local",
        ]

        if session_key:
            cmd.extend(["--session-key", session_key])

        cmd.extend(["--message", message])

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr)

        return result.stdout.strip()
