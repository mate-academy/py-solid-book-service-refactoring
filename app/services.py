from app.displays import Display
from app.models import Book
from app.printers import Printer
from app.serializers import Serializer


class SerializerService:
    def __init__(self, serializers: dict[str, Serializer]) -> None:
        self.serializers = serializers

    def get_serializer(self, serialize_type: str) -> Serializer:
        if serialize_type not in self.serializers:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return self.serializers[serialize_type]

    def execute(self, book: Book, serialize_type: str) -> str:
        serializer = self.get_serializer(serialize_type)
        return serializer.execute(book)


class PrinterService:
    def __init__(self, printers: dict[str, Printer]) -> None:
        self.printers = printers

    def get_printer(self, printer_type: str) -> Printer:
        if printer_type not in self.printers:
            raise ValueError(f"Unknown printer type: {printer_type}")
        return self.printers[printer_type]

    def execute(self, book: Book, printer_type: str) -> None:
        printer = self.get_printer(printer_type)
        printer.execute(book)


class DisplayService:
    def __init__(self, displays: dict[str, Display]) -> None:
        self.displays = displays

    def get_display(self, display_type: str) -> Display:
        if display_type not in self.displays:
            raise ValueError(f"Unknown display type: {display_type}")
        return self.displays[display_type]

    def execute(self, book: Book, display_type: str) -> None:
        display = self.get_display(display_type)
        display.execute(book)


class BookCommandService:
    def __init__(
        self,
        services: dict[
            str, DisplayService | PrinterService | SerializerService
        ]
    ) -> None:
        self.services = services

    def get_service(
        self, command: str
    ) -> DisplayService | PrinterService | SerializerService:
        if command not in self.services:
            raise ValueError(f"Unknown service type: {command}")
        return self.services[command]

    def execute_command(
            self,
            book: Book, command: tuple[str, str]
    ) -> None | str:
        cmd, method_type = command
        service = self.get_service(cmd)
        return service.execute(book, method_type)

    def run(self, book: Book, commands: list[tuple[str, str]]) -> None | str:
        for command in commands:
            result = self.execute_command(book, command)
            if result is not None:
                return result
