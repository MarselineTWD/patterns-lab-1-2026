from datetime import datetime

import pytest

from adapters import DigitalClockAdapter
from clocks import AnalogClock
from consts import DayNightDivision
from interfaces import BaseDigitalClock


@pytest.mark.parametrize(
    ("value", "day_part"),
    [
        (datetime(2026, 1, 1, 0, 0, 0), DayNightDivision.AM),
        (datetime(2026, 1, 1, 12, 0, 0), DayNightDivision.PM),
        (datetime(2026, 12, 31, 23, 59, 59), DayNightDivision.PM),
    ],
)
def test_adapter_converts_boundary_values(
    value: datetime, day_part: DayNightDivision
) -> None:
    analog_clock = AnalogClock()
    adapter = DigitalClockAdapter(analog_clock)

    adapter.set_date_time(value)

    assert adapter.get_date_time() == value
    assert analog_clock.get_day_night_division() is day_part


def test_adapter_converts_time_to_hand_angles() -> None:
    analog_clock = AnalogClock()
    adapter = DigitalClockAdapter(analog_clock)

    adapter.set_date_time(datetime(2026, 9, 24, 15, 30, 45))

    assert analog_clock.get_hour_angle() == 90.0
    assert analog_clock.get_minute_angle() == 180.0
    assert analog_clock.get_second_angle() == 270.0


def test_adapter_implements_digital_clock_interface() -> None:
    assert isinstance(DigitalClockAdapter(), BaseDigitalClock)
