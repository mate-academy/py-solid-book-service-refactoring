import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


class SerializerFactory:
    @staticmethod
    def get_serializer(serializer_type: str) -> Serializer:
        if serializer_type == "json":
            return JsonSerializer()
        elif serializer_type == "xml":
            return XmlSerializer()
        else:
            raise ValueError(f"Unknown serialize type: {serializer_type}")
