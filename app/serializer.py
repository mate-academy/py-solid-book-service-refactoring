import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod
from .book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({
            "title": book.title,
            "content": book.content
        })


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        content = ElementTree.SubElement(root, "content")

        return ElementTree.tostring(root, encoding="unicode")


SERIALIZERS = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def serialize_book(book: Book, serialize_type: str) -> str:
    if serialize_type not in SERIALIZERS:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
    return SERIALIZERS[serialize_type].serialize(book)
