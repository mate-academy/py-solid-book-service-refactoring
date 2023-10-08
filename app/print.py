from .book import Book
from .display import MethodType


class BookPrint(MethodType):
    def console(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)

    def reverse(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
