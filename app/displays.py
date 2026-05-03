from app.books import Book
from app.interfaces import DisplayBookInterface


class DisplayBook(DisplayBookInterface):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content)


class DisplayReversedBook(DisplayBook):
    def __init__(self, book: Book) -> None:
        super().__init__(book=book)

    def display(self) -> None:
        print(self.book.content[::-1])
