from typing import List, Tuple, Optional
from app.book import Book
from app.io_handlers import ConsoleWriter
from app.strategies import (
    ConsoleDisplay, ReverseDisplay,
    ConsolePrinter, ReversePrinter,
    JsonSerializer, XmlSerializer
)


class BookService:
    def __init__(self):
        writer = ConsoleWriter()

        self.display_strategies = {
            "console": ConsoleDisplay(writer),
            "reverse": ReverseDisplay(writer)
        }
        self.print_strategies = {
            "console": ConsolePrinter(writer),
            "reverse": ReversePrinter(writer)
        }
        self.serialize_strategies = {
            "json": JsonSerializer(),
            "xml": XmlSerializer()
        }

    def process(self, book: Book, commands: List[Tuple[str, str]]) -> Optional[str]:
        for cmd, method_type in commands:
            if cmd == "display":
                self.display_strategies[method_type].display(book)
            elif cmd == "print":
                self.print_strategies[method_type].print_book(book)
            elif cmd == "serialize":
                return self.serialize_strategies[method_type].serialize(book)
        return None
