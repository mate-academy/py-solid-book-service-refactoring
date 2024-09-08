import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod
from app.models import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JsonSerializer(Serializer):
    def __init__(self, serialize_type: str) -> None:
        self.serialize_type = serialize_type

    def serialize(self, book: Book) -> str:
        if self.serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        else:
            raise ValueError(f"Unknown serialize type: {self.serialize_type}")


class XmlSerializer(Serializer):
    def __init__(self, serialize_type: str) -> None:
        self.serialize_type = serialize_type

    def serialize(self, book: Book) -> str:
        if self.serialize_type == "xml":
            root = ElementTree.Element("book")
            title = ElementTree.SubElement(root, "title")
            title.text = book.title
            content = ElementTree.SubElement(root, "content")
            content.text = book.content
            return ElementTree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {self.serialize_type}")
