from typing import Any

from app.book import Book
from app.cmd_manager.display.manager import DisplayManager
from app.cmd_manager.print.manager import PrintManager
from app.cmd_manager.serialize.manager import SerializeManager
from app.validators import CommandValidatorMixin


class CommandManager(CommandValidatorMixin):
    def __init__(self, command: str, method_type: str, book: Book) -> None:
        self.command = command
        self.method_type = method_type
        self.book = book

    def execute_command(self) -> Any:
        self.validate_command(self.command)

        if self.command == "display":
            displayer = DisplayManager().set_displayer(self.method_type)
            displayer.display(self.book)

        elif self.command == "print":
            printer = PrintManager().set_printer(self.method_type)
            printer.print_book(self.book)

        elif self.command == "serialize":
            serializer = SerializeManager().set_serializer(self.method_type)
            return serializer.serialize(self.book)
