from typing import Type

from app.book.book_services.method_interface import IBookAction
from app.book.book_services.displayer import (
    BookDisplayerConsole,
    BookDisplayerReverse
)
from app.book.custom_exceptions.displayer_exceptions import (
    UnknownDisplayTypeError
)
from app.book.factories.method_factory_interface import BookMethodFactory


class BookDisplayerFactory(BookMethodFactory):
    @staticmethod
    def get_book_method(display_type: str) -> Type[IBookAction]:
        match display_type:
            case "console":
                return BookDisplayerConsole
            case "reverse":
                return BookDisplayerReverse
        raise UnknownDisplayTypeError(display_type)
