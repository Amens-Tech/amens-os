from dotenv import load_dotenv

load_dotenv()

from core.services.scheduler import Scheduler
from core.services.planner import Planner
from core.services.executor import Executor


def main():

    scheduler = Scheduler()

    if not scheduler.company_is_open():
        return

    planner = Planner()
    executor = Executor()

    event = planner.next_action()

    print(event)

    executor.execute(event)


if __name__ == "__main__":
    main()
