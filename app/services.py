from typing import List, Tuple
from .models import Book
from .displayers import ConsoleDisplay, ReverseDisplay
from .printers import ConsolePrinter, ReversePrinter
from .serializers import JsonSerializer, XmlSerializer


class BookService:
    DISPLAYERS = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    PRINTERS = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }

    SERIALIZERS = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    def __init__(self, book: Book):
        self.book = book

    def execute(self, commands: List[Tuple[str, str]]) -> str | None:
        for cmd, method_type in commands:
            if cmd == "display":
                self.DISPLAYERS[method_type].display(self.book)
            elif cmd == "print":
                self.PRINTERS[method_type].print_book(self.book)
            elif cmd == "serialize":
                return self.SERIALIZERS[method_type].serialize(self.book)
            else:
                raise ValueError(f"Unknown command: {cmd}")
