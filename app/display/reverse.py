from app.display.base import DisplayStrategy
from app.models import Book


class ReverseDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
