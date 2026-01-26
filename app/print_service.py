from app.enums import PrintType
from app.interfaces import HasTitleContent
from app.printer import PrintStrategy


class PrintService:
    def __init__(self, printers: dict[PrintType, PrintStrategy]) -> None:
        self.printers = printers

    def print(self, book: HasTitleContent, print_type: str) -> None:
        pt = PrintType.from_str(print_type)
        printer = self.printers.get(pt)

        if printer is None:
            raise ValueError(f"No printer found for type: {print_type}")

        printer.print_book(book)
