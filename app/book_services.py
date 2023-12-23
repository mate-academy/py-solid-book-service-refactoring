from __future__ import annotations

from app.displayer import ConsoleDisplayer, ReverseDisplayer
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JSONSerializer, XMLSerializer

from app.book_model import Book


def serialize_to_json(book: Book) -> str:
    return JSONSerializer.serialize(book)


def serializer_to_xml(book: Book) -> str:
    return XMLSerializer.serialize(book)


def print_console(book: Book) -> None:
    ConsolePrinter.print_book(book)


def print_reverse(book: Book) -> None:
    ReversePrinter.print_book(book)


def display_console(book: Book) -> None:
    ConsoleDisplayer.display_book(book)


def display_reverse(book: Book) -> None:
    ReverseDisplayer.display_book(book)
