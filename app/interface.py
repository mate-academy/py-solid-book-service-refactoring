import json
from typing import Protocol
import xml.etree.ElementTree as ET  # noqa

from app.models import Book


class IDisplayProcessor(Protocol):
    def display(self, book: Book) -> None:
        pass


class IPrintProcessor(Protocol):
    def print(self, book: Book) -> None:
        pass


class ISerializeProcessor(Protocol):
    def serialize(self, book: Book) -> str:
        pass


class ConsoleDisplayProcessor:
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayProcessor:
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class ConsolePrintProcessor:
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrintProcessor:
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class JsonSerializeProcessor:
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializeProcessor:
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
