import json
import xml.etree.ElementTree as ElementTree

from app.models import Book
from app.interface import DefaultInterface


class JsonSerializer(DefaultInterface):
    def run(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(DefaultInterface):
    def run(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
