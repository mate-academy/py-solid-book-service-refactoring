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
        self.validate_input()

    def validate_input(self) -> None:
        if self.command == "display":
            if self.method_type not in DISPLAY_PROCESSORS.keys():
                raise ValueError(f"Unknown display type: {self.method_type}")
        elif self.command == "print":
            if self.method_type not in PRINT_PROCESSORS.keys():
                raise ValueError(f"Unknown print type: {self.method_type}")
        elif self.command == "serialize":
            if self.method_type not in SERIALIZE_PROCESSORS.keys():
                raise ValueError(f"Unknown serialize type: {self.method_type}")

    def run_command(self) -> None:
        if self.command == "display":
            DISPLAY_PROCESSORS[self.method_type].display(self.book)
        elif self.command == "print":
            PRINT_PROCESSORS[self.method_type].print(self.book)
        elif self.command == "serialize":
            return SERIALIZE_PROCESSORS[self.method_type].serialize(self.book)
