import json
import xml.etree.ElementTree as ElementTree
from typing import Any

from app.book import Book


class Serializer:
    def __init__(self, book: Book, serialize_type: str) -> None:
        self.serialize_type = serialize_type
        self.book = book
        self.dispatch()

    def json(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )

    def xml(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.book.content
        return ElementTree.tostring(root, encoding="unicode")

    def dispatch(self) -> Any:
        if self.serialize_type == "xml":
            return self.xml()
        elif self.serialize_type == "json":
            return self.json()
        raise ValueError(f"Unknown serialize type: {self.serialize_type}")
