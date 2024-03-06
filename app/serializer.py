from abc import ABC, abstractmethod
from xml.etree import ElementTree as ET
from app.book import Book

import json


class SerializeFile(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(SerializeFile):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(SerializeFile):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content

        return ET.tostring(root, encoding="unicode")


serializer_handlers = {
    "json": JSONSerializer,
    "xml": XMLSerializer,
}
