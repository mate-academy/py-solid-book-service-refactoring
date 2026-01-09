import json
import xml.etree.ElementTree as Et
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.main import Book


class SerializerStrategy:
    def serialize(self, book: "Book") -> str:
        raise NotImplementedError


class JsonSerializer(SerializerStrategy):
    def serialize(self, book: "Book") -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializerStrategy):
    def serialize(self, book: "Book") -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(
            root, encoding="unicode"
        )
