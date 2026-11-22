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


SERIALIZERS: dict[str, Serializer] = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def get_serializer(serialize_type: str) -> Serializer:
    serializer = SERIALIZERS.get(serialize_type)
    if serializer is None:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
    return serializer
