from abc import ABC, abstractmethod

from app.book import Book
from app.display import ConsoleDisplay
from app.formater import NormalFormat, ReverseFormat
from app.serialize import JsonSerializer, XmlSerializer


class Command(ABC):
    @abstractmethod
    def execute(self, book: Book):
        pass


def get_formatter(method_type: str):
    formatters = {
        "console": NormalFormat,
        "reverse": ReverseFormat,
    }

    try:
        return formatters[method_type]()
    except KeyError:
        raise ValueError(f"Unknown formatter type: {method_type}")


class DisplayCommand(Command):
    def __init__(self, method_type: str) -> None:
        self.formatter = get_formatter(method_type)

    def execute(self, book: Book):
        display = ConsoleDisplay(self.formatter)
        display.display(book)


class PrintCommand(Command):
    def __init__(self, method_type: str) -> None:
        self.formatter = get_formatter(method_type)

        messages = {
            "console": "Printing the book: {}...",
            "reverse": "Printing the book in reverse: {}...",
        }

        try:
            self.message_template = messages[method_type]
        except KeyError:
            raise ValueError(f"Unknown print type: {method_type}")

    def execute(self, book: Book):
        print(self.message_template.format(book.title))
        print(self.formatter.format(book))


class SerializeCommand(Command):
    def __init__(self, method_type: str):
        serializers = {
            "json": JsonSerializer,
            "xml": XmlSerializer,
        }

        try:
            self.serializer = serializers[method_type]()
        except KeyError:
            raise ValueError(f"Unknown serialize type: {method_type}")

    def execute(self, book: Book):
        return self.serializer.serialize(book)
