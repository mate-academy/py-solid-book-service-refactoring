import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET

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
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


def serialize_command(book: Book, method_type: str) -> str:
    if method_type == "json":
        method_type = JSONSerialize()
    elif method_type == "xml":
        method_type = XMLSerialize()
    else:
        raise ValueError(f"Unknown serialize type: {method_type}")
    return method_type.serialize(book)
