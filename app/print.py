from typing import Any

from app.book import Book


class Print:
    def __init__(self, book: Book, print_type: str) -> None:
        self.print_type = print_type
        self.book = book
        self.dispatch()

    def console(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)

    def reverse(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])

    def dispatch(self) -> Any:
        if self.print_type == "console":
            return self.console()
        elif self.print_type == "reverse":
            return self.reverse()
        raise ValueError(f"Unknown display type: {self.print_type}")
