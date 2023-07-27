import json
import xml.etree.ElementTree as et

from app.main import Book


class BookSerialization:
    @staticmethod
    def serialize(book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif serialize_type == "xml":
            root = et.Element("book")
            title = et.SubElement(root, "title")
            title.text = book.title
            content = et.SubElement(root, "content")
            content.text = book.content
            return et.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
