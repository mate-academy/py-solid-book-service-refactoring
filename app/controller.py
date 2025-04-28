from models import Book
from interfaces import DisplayStrategy, PrintStrategy, SerializeStrategy


class BookController:
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self, strategy: DisplayStrategy) -> None:
        strategy.display(self.book.content)

    def print_book(self, strategy: PrintStrategy) -> None:
        strategy.print(self.book.title, self.book.content)

    def serialize(self, strategy: SerializeStrategy) -> str:
        return strategy.serialize(self.book.title, self.book.content)
