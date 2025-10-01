from __future__ import annotations

from services.ports import DisplayStrategy, BookLike


class ReverseDisplay(DisplayStrategy):
    def display(self, book: "BookLike") -> None:
        print(book.content[::-1])
