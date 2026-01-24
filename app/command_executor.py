from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JsonSerializer, XmlSerializer


class CommandExecutor:
    def __init__(self, book: Book) -> None:
        self.book = book

        self.display_strategies = {
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay(),
        }

        self.print_strategies = {
            "console": ConsolePrinter(),
            "reverse": ReversePrinter(),
        }

        self.serializer_strategies = {
            "json": JsonSerializer(),
            "xml": XmlSerializer(),
        }

    def execute(self, command: str, method_type: str) -> str | None:
        if command == "display":
            self.display_strategies[method_type].display(self.book)
            return None

        if command == "print":
            self.print_strategies[method_type].print_book(self.book)
            return None

        if command == "serialize":
            return self.serializer_strategies[method_type].serialize(self.book)

        raise ValueError(f"Unknown command: {command}")
