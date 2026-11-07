import json
import xml.etree.ElementTree as Et

from typing import TYPE_CHECKING
from app.interface import DisplayInterface, PrintInterface, SerializeInterface


if TYPE_CHECKING:
    from app.main import Book


class ConsoleDisplay(DisplayInterface):
    def display(self, book: "Book") -> None:
        print(book.content)


class ReverseDisplay(DisplayInterface):
    def display(self, book: "Book") -> None:
        print(book.content[::-1])


class ConsolePrint(PrintInterface):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintInterface):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class JsonSerialize(SerializeInterface):
    def serialize(self, book: Book) -> str:
        return json.dumps({
            "title": book.title,
            "content": book.content
        })


class XmlSerialize(SerializeInterface):
    def serialize(self, book: Book) -> str:
        book_element = Et.Element("book")
        title_element = Et.SubElement(book_element, "title")
        title_element.text = book.title
        content_element = Et.SubElement(book_element, "content")
        content_element.text = book.content

        return Et.tostring(book_element, encoding="unicode")
