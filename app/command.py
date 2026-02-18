from abc import ABC, abstractmethod

from app.display import Display
from app.print import Printer
from app.serializer import Serializer
from app.solid import Book


class Command(ABC):
    @abstractmethod
    def execute(self) -> None | str:
        pass


class DisplayCommand(Command):
    def __init__(self, display: Display) -> None:
        self.display = display

    def execute(self) -> None | str:
        return self.display.display()


class PrintCommand(Command):
    def __init__(self, printer: Printer) -> None:
        self.printer = printer

    def execute(self) -> None | str:
        return self.printer.print()


class SerializerCommand(Command):
    def __init__(self, serializer: Serializer, book: Book) -> None:
        self.serializer = serializer
        self.book = book

    def execute(self) -> None | str:
        return self.serializer.serialize(self.book.title, self.book.content)
