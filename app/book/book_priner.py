from app.book.book import Book
from app.book.display import Display


class Printer:
    def __init__(self, print_type: str) -> None:
        self._print_type = print_type

    @property
    def print_type(self) -> str:
        return self._print_type

    @print_type.setter
    def print_type(self, print_type: str) -> [None | ValueError]:
        if print_type in ("console", "reverse"):
            self._print_type = print_type
        else:
            raise ValueError(f"Unknown print type: {print_type}")

    def print(self, book: Book, display: "Display") -> None:
        message = (
            f"Printing the book in reverse: {book.title}..."
            if self.print_type != "console"
            else f"Printing the book: {book.title}..."
        )
        print(message)
        display.show_content(book)


def print_book(book: Book, print_type: str) -> None:
    display = Display(print_type)
    printer = Printer(print_type)

    printer.print(book, display)
