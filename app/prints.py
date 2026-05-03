from app.books import Book
from app.interfaces import PrintBookInterface


class PrintBook(PrintBookInterface):
    def __init__(self, book: Book) -> None:
        self.book = book

    def print_book(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class PrintReversedBook(PrintBook):
    def __init__(self, book: Book) -> None:
        super().__init__(book=book)

    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
