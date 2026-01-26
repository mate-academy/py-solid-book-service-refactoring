import json
import xml.etree.ElementTree as ElementTree
from .book import Book


class JsonSerializer:
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer:
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title_elem = ElementTree.SubElement(root, "title")
        title_elem.text = book.title
        content_elem = ElementTree.SubElement(root, "content")
        content_elem.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
