from dotenv import load_dotenv

load_dotenv()

from automation.scheduler import Scheduler
from automation.planner import Planner
from automation.executor import Executor


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
