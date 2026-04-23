from app.book import Book
from app.formatter import Formatter


class BookDisplayer:
    def display(self, book: Book, formatter: Formatter) -> None:
        print(formatter.format(book))
