import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod

from app.book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass


class JsonSerializer(BookSerializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class XmlSerializer(BookSerializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.book.content
        return ElementTree.tostring(root, encoding="unicode")


class SerializerFormat:
    @staticmethod
    def create_serializer(serializer_type: str, book: Book) -> BookSerializer:
        if serializer_type == "json":
            return JsonSerializer(book)
        elif serializer_type == "xml":
            return XmlSerializer(book)
