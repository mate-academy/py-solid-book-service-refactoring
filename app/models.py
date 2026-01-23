import json
import xml.etree.ElementTree as ElTree
from typing import Any

from app.abstract_models import Display, Print, Serializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class ConsoleDisplay(Display):
    def display(self, book: Any) -> None:
        print(book.content)


class ReversedDisplay(Display):
    def display(self, book: Any) -> None:
        print(book.content[::-1])


class ConsolePrint(Print):
    def print(self, book: Any) -> None:
        print(f"Printing the book: {book.title}...\n{book.content}")


class ReversedPrint(Print):
    def print(self, book: Any) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content[::-1])


class JsonSerializer(Serializer):
    def serialize(self, file_type: str, book: Book) -> str:
        return json.dumps(
            {
                "title": book.title,
                "content": book.content
            }
        )


class XMLSerializer(Serializer):
    def serialize(self, file_type: str, book: Book) -> str:
        root = ElTree.Element("book")
        title = ElTree.SubElement(root, "title")
        title.text = book.title
        content = ElTree.SubElement(root, "content")
        content.text = book.content
        return ElTree.tostring(root, encoding="unicode")
