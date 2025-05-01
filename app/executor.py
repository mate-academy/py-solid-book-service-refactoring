from app.book import Book
from app.display import DisplayBookConsole, DisplayBookReverse
from app.printer import PrintBookConsole, PrintBookReverse
from app.serializer import SerializeBookJson, SerializeBookXml


class CommandExecutor:
    def __init__(self) -> None:
        self.display_strategies = {
            "console": DisplayBookConsole(),
            "reverse": DisplayBookReverse(),
        }
        self.print_strategies = {
            "console": PrintBookConsole(),
            "reverse": PrintBookReverse(),
        }
        self.serialize_strategies = {
            "json": SerializeBookJson(),
            "xml": SerializeBookXml(),
        }

    def execute_display(self, method_type: str, book: Book) -> None:
        command = self.display_strategies.get(method_type)
        if command:
            command.display(book)
        else:
            raise ValueError(f"Unknown display type: {method_type}")

    def execute_print(self, method_type: str, book: Book) -> None:
        command = self.print_strategies.get(method_type)
        if command:
            command.print(book)
        else:
            raise ValueError(f"Unknown print type: {method_type}")

    def execute_serialize(self, method_type: str, book: Book) -> str:
        command = self.serialize_strategies.get(method_type)
        if command:
            return command.serialize(book)
        else:
            raise ValueError(f"Unknown serialize type: {method_type}")
