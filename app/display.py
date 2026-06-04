from typing import Any

from app.book import Book


class Display:
    def __init__(self, book: Book, display_type: str) -> None:
        self.display_type = display_type
        self.book = book
        self.dispatch()

    def console(self) -> None:
        print(self.book.content)

    def reverse(self) -> None:
        print(self.book.content[::-1])

    def dispatch(self) -> Any:
        if self.display_type == "console":
            return self.console()
        elif self.display_type == "reverse":
            return self.reverse()
        raise ValueError(f"Unknown display type: {self.display_type}")
