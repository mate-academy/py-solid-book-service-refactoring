from app.book_print import BookPrint, PrintConsole, PrintReverse
from app.exceptions import PrintTypeError


class PrintService:
    @staticmethod
    def get_print(print_type: str) -> BookPrint:
        if print_type == "console":
            return PrintConsole()
        elif print_type == "reverse":
            return PrintReverse()
        else:
            raise PrintTypeError(print_type)
