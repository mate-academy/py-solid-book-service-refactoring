import json
import xml.etree.ElementTree as ElTr

from .interfaces import ISerializer
from .models import Book


class JsonSerializer(ISerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(ISerializer):
    def serialize(self, book: Book) -> str:
        root = ElTr.Element("book")
        title = ElTr.SubElement(root, "title")
        title.text = book.title
        content = ElTr.SubElement(root, "content")
        content.text = book.content
        return ElTr.tostring(root, encoding="unicode")
