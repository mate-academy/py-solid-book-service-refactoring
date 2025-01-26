import json
import xml.etree.ElementTree as ETree
from abc import ABC, abstractmethod

from app.book import Book


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class SerializationStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class Console(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class Reverse(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class JSONSerializer(SerializationStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(SerializationStrategy):
    def serialize(self, book: Book) -> str:
        root = ETree.Element("book")
        title = ETree.SubElement(root, "title")
        title.text = book.title
        content = ETree.SubElement(root, "content")
        content.text = book.content
        return ETree.tostring(root, encoding="unicode")
