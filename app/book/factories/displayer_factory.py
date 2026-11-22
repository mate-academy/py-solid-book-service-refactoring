from app.book.book_services.displayer import (
    Displayer,
    DisplayerConsole,
    DisplayerReverse
)
from app.book.custom_exceptions.displayer_errors import UnknownDisplayTypeError


class DisplayerFactory:
    @staticmethod
    def get_displayer(display_type: str) -> Displayer:
        if display_type == "console":
            return DisplayerConsole()
        elif display_type == "reverse":
            return DisplayerReverse()
        else:
            raise UnknownDisplayTypeError(display_type)
