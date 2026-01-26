import json
import xml.etree.ElementTree as ET
from app.models import Book
from app.interfaces import ActionInterface


class JsonSerializer(ActionInterface):
    def execute(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(ActionInterface):
    def execute(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
