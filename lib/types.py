from typing import List
from typing import Any
from dataclasses import dataclass


@dataclass
class Wikipedium:
    title: str
    wikipedia: str

    @staticmethod
    def from_dict(obj: Any) -> "Wikipedium":
        _title = str(obj.get("title"))
        _wikipedia = str(obj.get("wikipedia"))
        return Wikipedium(_title, _wikipedia)


@dataclass
class Event:
    year: str
    description: str
    wikipedia: List[Wikipedium]

    @staticmethod
    def from_dict(obj: Any) -> "Event":
        _year = str(obj.get("year"))
        _description = str(obj.get("description"))
        _wikipedia = [Wikipedium.from_dict(y) for y in obj.get("wikipedia")]
        return Event(_year, _description, _wikipedia)


@dataclass
class ThisDayData:
    wikipedia: str
    date: str
    events: List[Event]

    @staticmethod
    def from_dict(obj: Any) -> "ThisDayData":
        _wikipedia = str(obj.get("wikipedia"))
        _date = str(obj.get("date"))
        _events = [Event.from_dict(y) for y in obj.get("events")]
        return ThisDayData(_wikipedia, _date, _events)
