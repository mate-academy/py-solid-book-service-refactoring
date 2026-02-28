from abc import ABC, abstractmethod
from app.models import Book
from app.services import FORMATTERS, SERIALIZERS


class Commands(ABC):
    @abstractmethod
    def command(self, book: Book, method_type: str) -> str | None:
        pass


class DisplayCommand(Commands):
    def command(self, book: Book, method_type: str) -> None:
        formatter = FORMATTERS.get(method_type)
        if not formatter:
            raise ValueError(f"Unknown display type: {method_type}")
        print(formatter.format(book))


class PrintCommand(Commands):
    def command(self, book: Book, method_type: str) -> None:
        formatter = FORMATTERS.get(method_type)
        if not formatter:
            raise ValueError(f"Unknown print type: {method_type}")
        if method_type == "console":
            print(f"Printing the book: {book.title}...")
        elif method_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
        print(formatter.format(book))


class SerializeCommand(Commands):
    def command(self, book: Book, method_type: str) -> str:
        serializer = SERIALIZERS.get(method_type)
        if not serializer:
            raise ValueError(f"Unknown serialize type: {method_type}")
        return serializer.serialize(book)


COMMANDS = {
    "display": DisplayCommand(),
    "print": PrintCommand(),
    "serialize": SerializeCommand(),
}
