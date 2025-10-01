from __future__ import annotations

from services.ports import PrintStrategy, BookLike


class PrintReverseError(RuntimeError):
    pass


class ReversePrint(PrintStrategy):
    def print(self, book: "BookLike") -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
