from app.book import Book
from app.display import DisplayStrategy
from app.print_strategy import PrintStrategy
from app.serializer import Serializer


class BookService:
    def __init__(self, book: Book):
        self.book = book

    def execute_display(self, strategy: DisplayStrategy) -> None:
        strategy.display(self.book.content)

    def execute_print(self, strategy: PrintStrategy) -> None:
        strategy.print_book(self.book.title, self.book.content)

    def execute_serialize(self, serializer: Serializer) -> str:
        return serializer.serialize(self.book)
