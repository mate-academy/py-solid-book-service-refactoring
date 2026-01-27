import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: "Book"): pass


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book: "Book") -> str: pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: "Book"):
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: "Book"):
        print(book.content[::-1])


class ConsolePrint(DisplayStrategy):
    def display(self, book: "Book"):
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(DisplayStrategy):
    def display(self, book: "Book"):
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializeJson(SerializeStrategy):
    def serialize(self, book: "Book") -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml(SerializeStrategy):
    def serialize(self, book: "Book") -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")