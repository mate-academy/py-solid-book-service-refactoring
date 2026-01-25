from app.models import Book
from app.display_service import DisplayService
from app.print_service import PrintService
from app.serialize_service import SerializeService


class BookCommandService:
    def __init__(self) -> None:
        self._display_service = DisplayService()
        self._print_service = PrintService()
        self._serialize_service = SerializeService()

    def display(self, book: Book, display_type: str) -> None:
        self._display_service.display(book, display_type)

    def print(self, book: Book, print_type: str) -> None:
        self._print_service.print(book, print_type)

    def serialize(self, book: Book, serialize_type: str) -> str:
        return self._serialize_service.serialize(book, serialize_type)
