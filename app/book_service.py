from app.book import Book
from app.display_writers import IDisplayWriter
from app.printers import IPrinter
from app.serializers import ISerializer


class BookService:
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self, method_type: str) -> None:
        IDisplayWriter.get_display(method_type).display(self.book)

    def print(self, method_type: str) -> None:
        IPrinter.get_printer(method_type).print(self.book)

    def serialize(self, method_type: str) -> str:
        return ISerializer.get_serializer(method_type).serialize(self.book)
