from __future__ import annotations

from enum import Enum


class Command(Enum):
    DISPLAY = "display"
    PRINT = "print"
    SERIALIZE = "serialize"

    @classmethod
    def from_str(cls, value: str) -> Command:
        try:
            normalized = value.lower()
        except AttributeError:
            raise ValueError(f"Unknown command: {value}")
        for member in cls:
            if member.value == normalized:
                return member
        raise ValueError(f"Unknown command: {value}")


class DisplayType(Enum):
    CONSOLE = "console"
    REVERSE = "reverse"

    @classmethod
    def from_str(cls, value: str) -> DisplayType:
        try:
            normalized = value.lower()
        except AttributeError:
            raise ValueError(f"Unknown display type: {value}")
        for member in cls:
            if member.value == normalized:
                return member
        raise ValueError(f"Unknown display type: {value}")


class PrintType(Enum):
    CONSOLE = "console"
    REVERSE = "reverse"

    @classmethod
    def from_str(cls, value: str) -> PrintType:
        try:
            normalized = value.lower()
        except AttributeError:
            raise ValueError(f"Unknown print type: {value}")
        for member in cls:
            if member.value == normalized:
                return member
        raise ValueError(f"Unknown print type: {value}")


class SerializeType(Enum):
    JSON = "json"
    XML = "xml"

    @classmethod
    def from_str(cls, value: str) -> SerializeType:
        try:
            normalized = value.lower()
        except AttributeError:
            raise ValueError(f"Unknown serialize type: {value}")
        for member in cls:
            if member.value == normalized:
                return member
        raise ValueError(f"Unknown serialize type: {value}")
