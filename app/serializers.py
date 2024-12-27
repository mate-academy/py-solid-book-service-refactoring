import json
import xml.etree.ElementTree as element_tree

from app.book import Book


def serialize(book: Book, serialize_type: str) -> str:
    if serialize_type == "json":
        return json.dumps({"title": book.title, "content": book.content})
    elif serialize_type == "xml":
        root = element_tree.Element("book")
        title = element_tree.SubElement(root, "title")
        title.text = book.title
        content = element_tree.SubElement(root, "content")
        content.text = book.content
        return element_tree.tostring(root, encoding="unicode")
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
