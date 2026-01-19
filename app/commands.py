from app.interfaces import (
    CommandInterface,
    DisplayInterface,
    PrinterInterface,
    SerializerInterface,
    DisplayType,
    PrintType,
    SerializeType
)
from app.models import Book


class DisplayCommand(CommandInterface):
    def __init__(
            self, display: DisplayInterface,
            method_type: DisplayType
    ) -> None:
        self.display = display
        self.method_type = method_type

    def execute(self, book: Book) -> None:
        self.display.display(book, self.method_type)


class PrintCommand(CommandInterface):
    def __init__(
            self, printer: PrinterInterface,
            method_type: PrintType
    ) -> None:
        self.printer = printer
        self.method_type = method_type

    def execute(self, book: Book) -> None:
        self.printer.print_book(book, self.method_type)


class SerializerCommand(CommandInterface):
    def __init__(
            self, serializer: SerializerInterface,
            method_type: SerializeType
    ) -> None:
        self.serializer = serializer
        self.method_type = method_type

    def execute(self, book: Book) -> str:
        return self.serializer.serialize(book, self.method_type)
