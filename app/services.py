import json
import xml.etree.ElementTree
from collections.abc import Callable

from app.models import Book

DisplayHandler = Callable[[Book], None]
PrintHandler = Callable[[Book], None]
Serializer = Callable[[Book], str]


def _display_console(book: Book) -> None:
    print(book.content)


def _display_reverse(book: Book) -> None:
    print(book.content[::-1])


def _print_console(book: Book) -> None:
    print(f"Printing the book: {book.title}...")
    print(book.content)


def _print_reverse(book: Book) -> None:
    print(f"Printing the book in reverse: {book.title}...")
    print(book.content[::-1])


def _serialize_json(book: Book) -> str:
    return json.dumps({"title": book.title, "content": book.content})


def _serialize_xml(book: Book) -> str:
    root = xml.etree.ElementTree.Element("book")
    title = xml.etree.ElementTree.SubElement(root, "title")
    title.text = book.title
    content = xml.etree.ElementTree.SubElement(root, "content")
    content.text = book.content
    return xml.etree.ElementTree.tostring(root, encoding="unicode")


DISPLAYERS = {
    "console": _display_console,
    "reverse": _display_reverse,
}

PRINTERS = {
    "console": _print_console,
    "reverse": _print_reverse,
}

SERIALIZERS = {
    "json": _serialize_json,
    "xml": _serialize_xml,
}


def display_book(book: Book, display_type: str) -> None:
    display_handler = DISPLAYERS.get(display_type)
    if display_handler is None:
        raise ValueError(f"Unknown display type: {display_type}")

    display_handler(book)


def print_book(book: Book, print_type: str) -> None:
    print_handler = PRINTERS.get(print_type)
    if print_handler is None:
        raise ValueError(f"Unknown print type: {print_type}")

    print_handler(book)


def serialize_book(book: Book, serialize_type: str) -> str:
    serializer = SERIALIZERS.get(serialize_type)
    if serializer is None:
        raise ValueError(f"Unknown serialize type: {serialize_type}")

    return serializer(book)
