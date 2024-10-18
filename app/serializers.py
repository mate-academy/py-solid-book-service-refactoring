import json
import xml.etree.ElementTree as ElTree

from app.models import Book


class JsonSerializer:
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer:
    @staticmethod
    def serialize(book: Book) -> str:
        root = ElTree.Element("book")
        title = ElTree.SubElement(root, "title")
        title.text = book.title
        content = ElTree.SubElement(root, "content")
        content.text = book.content
        return ElTree.tostring(root, encoding="unicode")


class Serializer:
    @staticmethod
    def serialize(book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return JsonSerializer.serialize(book)
        elif serialize_type == "xml":
            return XmlSerializer.serialize(book)
        raise ValueError(f"Unknown serialize type: {serialize_type}")
