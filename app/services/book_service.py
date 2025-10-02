from app.models.book import Book
from app.strategies.display import IDisplayStrategy
from app.strategies.print_book import IPrintStrategy
from app.strategies.serialize import ISerializeStrategy


class BookService:
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self, strategy: IDisplayStrategy) -> None:
        strategy.display(self.book)

    def print_book(self, strategy: IPrintStrategy) -> None:
        strategy.print_book(self.book)

    def serialize(self, strategy: ISerializeStrategy) -> str:
        return strategy.serialize(self.book)
