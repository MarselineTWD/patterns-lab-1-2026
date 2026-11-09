from datetime import datetime

from clocks import AnalogClock
from consts import DayNightDivision
from interfaces import BaseAnalogClock, BaseDigitalClock


class DigitalClockAdapter(BaseDigitalClock):

    def __init__(self, analog_clock: BaseAnalogClock | None = None) -> None:
        self._analog_clock = analog_clock if analog_clock is not None else AnalogClock()

    def set_date_time(self, date: datetime) -> None:
        #Перевод обычного времени в углы стрелок с AM/PM.
        hour_angle = (date.hour % 12) * 30.0
        minute_angle = date.minute * 6.0
        second_angle = date.second * 6.0
        day_part = DayNightDivision.AM if date.hour < 12 else DayNightDivision.PM

        self._analog_clock.set_date_time(
            year=date.year,
            month=date.month,
            day=date.day,
            hour_angle=hour_angle,
            minute_angle=minute_angle,
            second_angle=second_angle,
            day_night_division=day_part,
        )

    def get_date_time(self) -> datetime:
        #Перевод углов стрелок и AM/PM обратно в обычное время
        hour_12 = round(self._analog_clock.get_hour_angle() / 30.0) % 12
        minute = round(self._analog_clock.get_minute_angle() / 6.0) % 60
        second = round(self._analog_clock.get_second_angle() / 6.0) % 60

        if self._analog_clock.get_day_night_division() is DayNightDivision.PM:
            hour = hour_12 + 12
        else:
            hour = hour_12

        return datetime(
            self._analog_clock.get_year(),
            self._analog_clock.get_month(),
            self._analog_clock.get_day(),
            hour,
            minute,
            second,
        )
