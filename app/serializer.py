import json
import xml.etree.ElementTree as eT

from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @property
    @abstractmethod
    def serialize(self) -> str:
        pass


class JsonSerializer(Serializer):
    @property
    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class XmlSerializer(Serializer):
    @property
    def serialize(self) -> str:
        root = eT.Element("book")
        title = eT.SubElement(root, "title")
        title.text = self.book.title
        content = eT.SubElement(root, "content")
        content.text = self.book.content
        return eT.tostring(root, encoding="unicode")


def serialize_book(book: Book, method_type: str) -> str:
    mappings = {"json": JsonSerializer, "xml": XmlSerializer}
    serializer = mappings.get(method_type)
    if serializer:
        return serializer(book).serialize
    else:
        raise ValueError(f"Unknown serialization type: {method_type}")
