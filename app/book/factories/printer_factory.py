from typing import Type

from app.book.book_services.method_interface import IBookAction
from app.book.book_services.printer import (
    BookPrinterConsole,
    BookPrinterReverse
)
from app.book.custom_exceptions.printer_exceptions import UnknownPrintTypeError
from app.book.factories.method_factory_interface import BookMethodFactory


class BookPrinterFactory(BookMethodFactory):
    @staticmethod
    def get_book_method(print_type: str) -> Type[IBookAction]:
        match print_type:
            case "console":
                return BookPrinterConsole
            case "reverse":
                return BookPrinterReverse
        raise UnknownPrintTypeError(print_type)
