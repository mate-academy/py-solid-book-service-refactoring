from app.models import Book
from app.display_service import DisplayService
from app.print_service import PrintService
from app.serialize_service import SerializeService


class BookCommandService:
    def __init__(
        self,
        display_service: DisplayService,
        print_service: PrintService,
        serialize_service: SerializeService
    ) -> None:
        self._display_service = display_service
        self._print_service = print_service
        self._serialize_service = serialize_service

    def display(self, book: Book, display_type: str) -> None:
        self._display_service.display(book, display_type)

    def print(self, book: Book, print_type: str) -> None:
        self._print_service.print(book, print_type)

    def serialize(self, book: Book, serialize_type: str) -> str:
        return self._serialize_service.serialize(book, serialize_type)
