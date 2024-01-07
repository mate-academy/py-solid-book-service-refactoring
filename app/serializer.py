import json
import xml.etree.ElementTree as Et
from app.book import Book


class JsonSerializer:
    @staticmethod
    def serialize(book: Book) -> json:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer:
    @staticmethod
    def serialize(book: Book) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")
