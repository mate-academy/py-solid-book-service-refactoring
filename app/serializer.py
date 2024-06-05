import json
import xml.etree.ElementTree as Et

from app.book import Book


class BookSerializer:
    @staticmethod
    def serialize(book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif serialize_type == "xml":
            root = Et.Element("book")
            title = Et.SubElement(root, "title")
            title.text = book.title
            content = Et.SubElement(root, "content")
            content.text = book.content
            return Et.tostring(root, encoding="unicode")
        raise ValueError(f"Unknown serialize type: {serialize_type}")
