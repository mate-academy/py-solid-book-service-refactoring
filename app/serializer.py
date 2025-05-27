import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod
from .book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


class SerializerFactory:
    @staticmethod
    def create_serializer(serialize_type: str) -> BookSerializer:
        if serialize_type == "json":
            return JsonSerializer()
        elif serialize_type == "xml":
            return XmlSerializer()
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
