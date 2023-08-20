import json
import xml.etree.ElementTree as ETree

from app.book import Book


class Serialization:
    @staticmethod
    def serialize(book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif serialize_type == "xml":
            root = ETree.Element("book")
            title_element = ETree.SubElement(root, "title")
            title_element.text = book.title
            content_element = ETree.SubElement(root, "content")
            content_element.text = book.content
            return ETree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
