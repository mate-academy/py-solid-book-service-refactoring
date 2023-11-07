from app.display_processor import (
    DisplayConsoleProcessor,
    DisplayReverseProcessor
)
from app.print_processor import PrintConsoleProcessor, PrintReverseProcessor
from app.serialize_process import SerializeXMLProcessor, SerializeJSONProcessor
from app.book import Book


DISPLAY_PROCESSORS = {
    "console": DisplayConsoleProcessor,
    "reverse": DisplayReverseProcessor
}

PRINT_PROCESSORS = {
    "console": PrintConsoleProcessor,
    "reverse": PrintReverseProcessor
}

SERIALIZE_PROCESSORS = {
    "json": SerializeJSONProcessor,
    "xml": SerializeXMLProcessor
}


class BookProcessor:
    def __init__(self, book: Book, command: str, method_type: str) -> None:
        self.book = book
        self.command = command
        self.method_type = method_type

    def run_command(self) -> None:
        if self.command == "display":
            if self.method_type not in DISPLAY_PROCESSORS.keys():
                raise ValueError(f"Unknown display type: {self.method_type}")
            DISPLAY_PROCESSORS[self.method_type](self.book).display()
        elif self.command == "print":
            if self.method_type not in PRINT_PROCESSORS.keys():
                raise ValueError(f"Unknown print type: {self.method_type}")
            PRINT_PROCESSORS[self.method_type](self.book).print()
        elif self.command == "serialize":
            if self.method_type not in SERIALIZE_PROCESSORS.keys():
                raise ValueError(f"Unknown serialize type: {self.method_type}")
            return SERIALIZE_PROCESSORS[self.method_type](self.book).serialize()
