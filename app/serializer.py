import json
import xml.etree.ElementTree as ET
from app.book import Book


class SerializerBook:
    def __init__(self, book: Book, serialize_type: str) -> None:
        self.book = book
        self.serialize_type = serialize_type

    def serialize(self) -> str:
        if self.serialize_type == "json":
            return json.dumps({"title": self.book.title, "content": self.book.content})
        elif self.serialize_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = self.book.title
            content = ET.SubElement(root, "content")
            content.text = self.book.content
            return ET.tostring(root, encoding="unicode")
