import json
import xml.etree.ElementTree as ET # noqa

from app.interfaces import SerializerBookInterface
from app.models import Book


class JsonSerializer(SerializerBookInterface):
    def serializer_book(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(SerializerBookInterface):
    def serializer_book(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
