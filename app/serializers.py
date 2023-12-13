import json
import xml.etree.ElementTree as ET
from typing import Any


class BookSerializer:
    @staticmethod
    def serialize(book: Any, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif serialize_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = book.title
            content = ET.SubElement(root, "content")
            content.text = book.content
            return ET.tostring(root, encoding="unicode")
        raise ValueError(f"Unknown serialize type: {serialize_type}")
