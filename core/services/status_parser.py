class StatusParser:

    @staticmethod
    def parse(reply):

        first = reply.strip().splitlines()[0].strip().upper()

        if first.startswith("STATUS:"):
            return first.replace("STATUS:", "").strip()

        return "UNKNOWN"
