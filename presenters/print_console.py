from __future__ import annotations

from services.ports import PrintStrategy, BookLike


class ConsolePrint(PrintStrategy):
    def print(self, book: "BookLike") -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)
