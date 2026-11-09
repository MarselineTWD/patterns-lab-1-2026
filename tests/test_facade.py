from datetime import datetime

from facades import ClockFacade


def test_facade_sets_gets_and_formats_time() -> None:
    clock = ClockFacade()
    value = datetime(2026, 9, 24, 12, 34, 56)

    clock.set_date_time(value)

    assert clock.get_date_time() == value
    assert clock.get_formatted_date_time() == "24.09.2026 12:34:56"
    assert clock.get_formatted_date_time("%Y/%m/%d") == "2026/09/24"


def test_facade_saves_every_change_in_history() -> None:
    clock = ClockFacade()
    first = datetime(2026, 9, 24, 8, 0, 0)
    second = datetime(2026, 9, 24, 18, 30, 10)

    clock.set_date_time(first)
    clock.set_date_time(second)

    assert clock.get_history() == (first, second)
