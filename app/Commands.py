from abc import ABC, abstractmethod
from typing import Mapping

from app.Displayers import Displayer
from app.Models import Book
from app.Printers import Printer
from app.Serializers import Serializer, get_strategy


class Command(ABC):
    @abstractmethod
    def execute(self, book: Book, method_type: str) -> str | None:
        pass


class DisplayCommand(Command):
    def __init__(self, displayers: Mapping[str, Displayer]) -> None:
        self._displayers = displayers

    def execute(self, book: Book, method_type: str) -> None:
        displayer = get_strategy(self._displayers, method_type, "display")
        displayer.display(book)


class PrintCommand(Command):
    def __init__(self, printers: Mapping[str, Printer]) -> None:
        self._printers = printers

    def execute(self, book: Book, method_type: str) -> None:
        printer = get_strategy(self._printers, method_type, "print")
        printer.print_book(book)


class SerializeCommand(Command):
    def __init__(self, serializers: Mapping[str, Serializer]) -> None:
        self._serializers = serializers

    def execute(self, book: Book, method_type: str) -> str:
        serializer = get_strategy(
            self._serializers, method_type, "serialize"
        )
        return serializer.serialize(book)
