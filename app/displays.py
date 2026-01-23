from typing import Any

from app.abstract_models import Display


class ConsoleDisplay(Display):
    def display(self, book: Any) -> None:
        print(book.content)


class ReversedDisplay(Display):
    def display(self, book: Any) -> None:
        print(book.content[::-1])
