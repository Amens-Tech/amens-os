from automation.scheduler import Scheduler
from automation.planner import Planner


def main():

    scheduler = Scheduler()

    if not scheduler.company_is_open():
        print("Company closed")
        return

    planner = Planner()

    event = planner.next_action()

    print("=" * 60)
    print("NEXT ACTION")
    print("=" * 60)
    print(event)
    print("=" * 60)


if __name__ == "__main__":
    main()
