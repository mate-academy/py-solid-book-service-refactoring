from __future__ import annotations
from interfaces import DisplayStrategy, BookDTO


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: BookDTO) -> None:
        # еквівалентно старому display("console")
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: BookDTO) -> None:
        # еквівалентно старому display("reverse")
        print(book.content[::-1])
