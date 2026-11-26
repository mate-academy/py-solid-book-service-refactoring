from app.book_display import Display, DisplayConsole, DisplayReverse
from app.exceptions import DisplayTypeError


class DisplayService:
    @staticmethod
    def get_display(display_type: str) -> Display:
        if display_type == "console":
            return DisplayConsole()
        elif display_type == "reverse":
            return DisplayReverse()
        else:
            raise DisplayTypeError(display_type)
