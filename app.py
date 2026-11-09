from datetime import datetime

from facades import ClockFacade


def main() -> None:
    clock = ClockFacade()
    current_time = datetime.now().replace(microsecond=0)

    clock.set_date_time(current_time)

    print(f"Дата и время: {clock.get_date_time()}")
    print(f"Красивый формат: {clock.get_formatted_date_time()}")
    print(f"Записей в истории: {len(clock.get_history())}")


if __name__ == "__main__":
    main()
