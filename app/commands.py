from abc import ABC, abstractmethod
from strategies import (
    ConsoleDisplay,
    ReverseDisplay,
    ConsolePrint,
    ReversePrint,
    SerializeJson,
    SerializeXml
)
from models import Book


class Command(ABC):
    @abstractmethod
    def execute(self, book: Book, method_type: str) -> str | None:
        pass


class DisplayCommand(Command):
    def __init__(self) -> None:
        self._strategies = {
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay(),
        }

    def execute(self, book: Book, method_type: str) -> None:
        strategy = self._strategies.get(method_type)
        if not strategy:
            raise ValueError(f"Unknow display type: {method_type}")
        strategy.display(book)


class PrintCommand(Command):
    def __init__(self) -> None:
        self._strategies = {
            "console": ConsolePrint(),
            "reverse": ReversePrint(),
        }

    def execute(self, book: Book, method_type: str) -> None:
        strategy = self._strategies.get(method_type)
        if not strategy:
            raise ValueError(f"Unknow print type: {method_type}")
        strategy.display(book)


class SerializeCommand(Command):
    def __init__(self) -> None:
        self._strategies = {
            "json": SerializeJson(),
            "xml": SerializeXml(),
        }

    def execute(self, book: Book, method_type: str) -> str:
        strategy = self._strategies.get(method_type)
        if not strategy:
            raise ValueError(f"Unknow serialization type: {method_type}")
        return strategy.serialize(book)


COMMANDS = {
    "display": DisplayCommand(),
    "print": PrintCommand(),
    "serialize": SerializeCommand(),
}
