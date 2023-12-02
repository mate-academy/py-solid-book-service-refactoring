import json
import xml.etree.ElementTree as ET
from app.book import Book


class Serializer:
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps(
                {"title": self.book.title, "content": self.book.content}
            )
        elif serialize_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = self.book.title
            content = ET.SubElement(root, "content")
            content.text = self.book.content
            return ET.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
