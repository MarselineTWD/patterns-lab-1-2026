from datetime import datetime

from adapters import DigitalClockAdapter 
from interfaces import BaseDigitalClock
from services import ClockFormatter, ClockHistory


class ClockFacade:


    def __init__(
        self,
        adapter: BaseDigitalClock | None = None,
        formatter: ClockFormatter | None = None,
        history: ClockHistory | None = None,
    ) -> None:
        self._adapter = adapter if adapter is not None else DigitalClockAdapter()
        self._formatter = formatter if formatter is not None else ClockFormatter()
        self._history = history if history is not None else ClockHistory()

    def set_date_time(self, value: datetime) -> None:
        #установка времени и сохранение его
        self._adapter.set_date_time(value)
        self._history.add(self._adapter.get_date_time())

    def get_date_time(self) -> datetime:
        #возврат текущего времени
        return self._adapter.get_date_time()

    def get_formatted_date_time(self, fmt: str = "%d.%m.%Y %H:%M:%S") -> str:
        #вовзврат текущего временеи в виде строки
        return self._formatter.format(self.get_date_time(), fmt)

    def get_history(self) -> tuple[datetime, ...]:
        #возврат истории изменений времени
        return self._history.all()
