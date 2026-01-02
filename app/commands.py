from .models import Book
from .display import DisplayStrategy
from .printers import Printer
from .serializers import Serializer


def execute_display(book: Book, display: DisplayStrategy) -> None:
    display.display(book)


def execute_print(book: Book, printer: Printer) -> None:
    printer.print_book(book)


def execute_serialize(book: Book, serializer: Serializer) -> str:
    return serializer.serialize(book)
