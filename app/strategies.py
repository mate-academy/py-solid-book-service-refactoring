import json
import xml.etree.ElementTree as elementTree

from .models import (
    Book,
    DisplayStrategy,
    PrintStrategy,
    SerializationStrategy
)


class ConsoleDisplayStrategy(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplayStrategy(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


class ConsolePrintStrategy(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrintStrategy(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class JsonSerializationStrategy(SerializationStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializationStrategy(SerializationStrategy):
    def serialize(self, book: Book) -> str:
        root = elementTree.Element("book")
        title = elementTree.SubElement(root, "title")
        title.text = book.title
        content = elementTree.SubElement(root, "content")
        content.text = book.content
        return elementTree.tostring(root, encoding="unicode")
