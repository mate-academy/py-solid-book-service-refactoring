import json
import xml.etree.ElementTree as ET  # noqa: N817

from abc import ABC, abstractmethod

from app.models import Book


class Serializer(ABC):
    @abstractmethod
    def execute(self, book: Book) -> str:
        pass


class JSONSerializer(Serializer):
    def execute(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):
    def execute(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
