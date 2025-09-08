from display.base import Display
from models.book import Book


class DisplayReverse(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
