from __future__ import annotations
from enum import Enum


class StringEnum(Enum):
    @classmethod
    def from_str(cls, value: str) -> StringEnum:
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"Invalid {cls.__name__}: {value}")


class Command(StringEnum):
    DISPLAY = "display"
    PRINT = "print"
    SERIALIZE = "serialize"


class DisplayType(StringEnum):
    CONSOLE = "console"
    REVERSE = "reverse"


class PrintType(StringEnum):
    CONSOLE = "console"
    REVERSE = "reverse"


class SerializeType(StringEnum):
    JSON = "json"
    XML = "xml"
