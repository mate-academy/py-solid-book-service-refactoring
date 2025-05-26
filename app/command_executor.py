from abc import ABC

from app.book import Book
from app.displayer import IBookDisplayer, select_displayer
from app.printer import IBookPrinter, select_printer
from app.serializer import IBookSerializer, select_serializer


class CommandExecutor(ABC):
    def __init__(self, cmd: str, method_type: str, book: Book) -> None:
        self.command_executor: (
            IBookPrinter | IBookDisplayer | IBookSerializer
        ) = None

        if cmd == "display":
            self.command_executor = select_displayer(method_type)(book)
        elif cmd == "print":
            self.command_executor = select_printer(method_type)(book)
        elif cmd == "serialize":
            self.command_executor = select_serializer(method_type)(book)

    def run(self) -> str | None:
        if isinstance(self.command_executor, IBookPrinter):
            self.command_executor.print()
        elif isinstance(self.command_executor, IBookDisplayer):
            self.command_executor.display()
        elif isinstance(self.command_executor, IBookSerializer):
            return self.command_executor.serialize()

        return None
