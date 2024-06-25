import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod

from .book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")


class BookSerializer:
    @staticmethod
    def serialize(book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return JSONSerializer().serialize(book)
        elif serialize_type == "xml":
            return XMLSerializer().serialize(book)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
