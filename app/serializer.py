import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod

from app.book import Book


class SerializerBehavior(ABC):

    @abstractmethod
    def serialize_book(self, book: Book) -> None:
        raise NotImplementedError


class JsonSerializer(SerializerBehavior):

    def serialize_book(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(SerializerBehavior):

    def serialize_book(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


def serialize_book(serialize_type: str) -> SerializerBehavior:
    if serialize_type == "json":
        return JsonSerializer()
    elif serialize_type == "xml":
        return XMLSerializer()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
