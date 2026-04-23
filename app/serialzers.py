import json
import xml.etree.ElementTree as Etree

from app.book import Book


class JsonSerializer:
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer:
    def serialize(self, book: Book) -> str:
        root = Etree.Element("book")
        title = Etree.SubElement(root, "title")
        title.text = book.title
        content = Etree.SubElement(root, "content")
        content.text = book.content
        return Etree.tostring(root, encoding="unicode")
