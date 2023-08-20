import json
import xml.etree.ElementTree as elementTree

from app.book import Book


class Serializer:
    def serialize(self, book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return self.serialize_json(book)
        elif serialize_type == "xml":
            return self.serialize_xml(book)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

    def serialize_json(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

    def serialize_xml(self, book: Book) -> str:
        root = elementTree.Element("book")
        title = elementTree.SubElement(root, "title")
        title.text = book.title
        content = elementTree.SubElement(root, "content")
        content.text = book.content
        return elementTree.tostring(root, encoding="unicode")
