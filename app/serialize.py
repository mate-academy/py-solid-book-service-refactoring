import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree

from app.book import Book


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


def serialize_command(book: Book, method_type: str) -> str:
    if method_type == "json":
        method_type = JSONSerialize()
    elif method_type == "xml":
        method_type = XMLSerialize()
    else:
        raise ValueError(f"Unknown serialize type: {method_type}")
    return method_type.serialize(book)
