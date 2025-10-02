from .displays import IDisplay
from .printers import IPrint
from .serializers import ISerializer
from .book import Book


class BookService:
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self, strategy: IDisplay) -> None:
        strategy.display(self.book)

    def print(self, strategy: IPrint) -> None:
        strategy.print(self.book)

    def serialize(self, serializer: ISerializer) -> str:
        return serializer.serialize(self.book)
