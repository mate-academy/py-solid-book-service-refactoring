from app.enums import PrintType
from app.interfaces import HasTitleContent
from app.printer import ConsolePrinter, ReversePrinter


class PrintService:
    def print(self, book: HasTitleContent, print_type: str) -> None:
        pt = PrintType.from_str(print_type)
        match pt:
            case PrintType.CONSOLE:
                ConsolePrinter().print_book(book)
            case PrintType.REVERSE:
                ReversePrinter().print_book(book)
