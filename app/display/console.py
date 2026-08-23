from app.book import Book
from app.display.base import Display


class ConsoleDisplay(Display):
    def display_content(self, book: "Book") -> None:
        print(book.content)
