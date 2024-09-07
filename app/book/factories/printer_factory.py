from app.book.book_services.printer import (
    Printer,
    PrinterConsole,
    PrinterReverse
)
from app.book.custom_exceptions.printer_errors import UnknownPrintTypeError


class PrinterFactory:
    @staticmethod
    def get_printer(print_type: str) -> Printer:
        if print_type == "console":
            return PrinterConsole()
        elif print_type == "reverse":
            return PrinterReverse()
        else:
            raise UnknownPrintTypeError(print_type)
