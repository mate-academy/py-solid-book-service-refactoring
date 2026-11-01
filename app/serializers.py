import json
from typing import Protocol

from app.book import Book
from xml.etree.ElementTree import Element, SubElement, tostring


class SerializeStrategy(Protocol):
    def serialize(self, book: Book) -> str:
        ...


class JsonSerialize:
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialize:
    def serialize(self, book: Book) -> str:
        root = Element("book")
        title = SubElement(root, "title")
        title.text = book.title
        content = SubElement(root, "content")
        content.text = book.content
        return tostring(root, encoding="unicode")
