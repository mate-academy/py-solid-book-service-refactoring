from abc import ABC, abstractmethod

from app.display import ReverseDisplay, ConsoleDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JsonSerialize, XmlSerialize
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.main import Book


class Command(ABC):
    @abstractmethod
    def execute(self, book: "Book") -> None:
        pass


class DisplayCommand(Command):
    def __init__(self, display: ConsoleDisplay | ReverseDisplay) -> None:
        self.display = display

    def execute(self, book: "Book") -> None:
        self.display.display(book)


class PrintCommand(Command):
    def __init__(self, printer: ConsolePrinter | ReversePrinter) -> None:
        self.printer = printer

    def execute(self, book: "Book") -> None:
        self.printer.print_book(book)


class SerializeCommand(Command):
    def __init__(self, serialize: JsonSerialize | XmlSerialize) -> None:
        self.serialize = serialize

    def execute(self, book: "Book") -> str:
        return self.serialize.serialize(book)

