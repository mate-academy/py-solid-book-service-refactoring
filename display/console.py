from display.base import Display
from models.book import Book


class DisplayConsole(Display):
    def display(self, book: Book) -> None:
        print(book.content)
