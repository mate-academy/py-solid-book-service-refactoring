import json
from typing import Protocol
from xml.etree.ElementTree import Element, SubElement, tostring

from app.models import Book


class Serializer(Protocol):
    def serialize(self, book: Book) -> str:
        ...


class JsonSerializer:
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer:
    def serialize(self, book: Book) -> str:
        root = Element("book")
        title = SubElement(root, "title")
        title.text = book.title
        content = SubElement(root, "content")
        content.text = book.content
        return tostring(root, encoding="unicode")
