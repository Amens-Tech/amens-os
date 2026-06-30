from automation.scheduler import Scheduler
from automation.planner import Planner
from automation.executor import Executor


def main():

    scheduler = Scheduler()

    if not scheduler.company_is_open():
        print("Company closed")
        return

    planner = Planner()
    executor = Executor()

    event = planner.next_action()

    result = executor.execute(event)

    print("=" * 70)
    print("EVENT")
    print("=" * 70)
    print(event)
    print()

    print("=" * 70)
    print("EXECUTION")
    print("=" * 70)

    for k, v in result.items():
        print(f"{k}: {v}")

    print("=" * 70)


if __name__ == "__main__":
    main()
