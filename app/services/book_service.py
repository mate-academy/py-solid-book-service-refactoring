from dataclasses import dataclass
from typing import Callable, Optional

from app.contracts import BookProtocol
from app.display.registry import get_displayer
from app.display.base import Displayer
from app.printing.registry import get_printer
from app.printing.base import Printer
from app.serialization.registry import get_serializer
from app.serialization.base import Serializer


@dataclass(frozen=True)
class BookService:
    displayer_resolver: Callable[[str], Displayer] = get_displayer
    printer_resolver: Callable[[str], Printer] = get_printer
    serializer_resolver: Callable[[str], Serializer] = get_serializer

    def execute(
        self, book: BookProtocol, commands: list[tuple[str, str]]
    ) -> Optional[str]:
        for cmd, method_type in commands:
            if cmd == "display":
                displayer = self.displayer_resolver(method_type)
                displayer.display(book)
            elif cmd == "print":
                printer = self.printer_resolver(method_type)
                printer.print(book)
            elif cmd == "serialize":
                serializer = self.serializer_resolver(method_type)
                return serializer.serialize(book)
        return None
