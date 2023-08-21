from app.entities.book import Book
from app.printers.printers import (
    ConsolePrinter,
    ReversePrinter
)


class PrintDispatcher:
    ALLOWED_PRINTERS = {
        "console": ConsolePrinter,
        "reverse": ReversePrinter
    }

    def handle(self, method_type: str, book: Book) -> None:
        if self.__is_print_type_valid(method_type):
            return self.ALLOWED_PRINTERS[method_type](
                book
            ).print()
        raise ValueError(f"Unknown print type: {method_type}")

    def __is_print_type_valid(self, method_type: str) -> bool:
        return method_type in self.ALLOWED_PRINTERS
