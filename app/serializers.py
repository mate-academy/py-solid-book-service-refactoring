import json
import xml.etree.ElementTree as et  # noqa: N813
from app.models import Book


class JsonSerializer:
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer:
    def serialize(self, book: Book) -> str:
        root = et.Element("book")
        title = et.SubElement(root, "title")
        title.text = book.title
        content = et.SubElement(root, "content")
        content.text = book.content
        return et.tostring(root, encoding="unicode")
