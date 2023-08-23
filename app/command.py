from abc import ABC, abstractmethod

from app.book import Book
from app.display import Display
from app.print import Print
from app.serialize import Serialize


class Command(ABC):
    @abstractmethod
    def execute(self, book: Book) -> None:
        pass


class DisplayCommand(Command):
    def __init__(self, display_type: str) -> None:
        self.display_type = display_type
        self.display_handler = Display()

    def execute(self, book: Book) -> None:
        return self.display_handler.get_display_type(book, self.display_type)


class PrintCommand(Command):
    def __init__(self, print_type: str) -> None:
        self.print_type = print_type
        self.print_handler = Print()

    def execute(self, book: Book) -> None:
        return self.print_handler.get_print_type(book, self.print_type)


class SerializeCommand(Command):
    def __init__(self, serialize_type: str) -> None:
        self.serialize_type = serialize_type
        self.serialize_handler = Serialize()

    def execute(self, book: Book) -> str:
        return self.serialize_handler.get_serialize(book, self.serialize_type)
