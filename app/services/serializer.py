from __future__ import annotations
import json
from xml.etree.ElementTree import Element, SubElement, tostring
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.book import Book


class JsonSerializer:
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer:
    @staticmethod
    def serialize(book: Book) -> str:
        root = Element("book")
        title_elem = SubElement(root, "title")
        title_elem.text = book.title
        content_elem = SubElement(root, "content")
        content_elem.text = book.content
        return tostring(root, encoding="utf-8").decode("utf-8")
