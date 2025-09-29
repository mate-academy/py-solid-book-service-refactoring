from app.display.base import DisplayStrategy
from app.models import Book


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)
