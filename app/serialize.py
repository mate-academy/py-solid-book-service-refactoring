import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

from app.models import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: "Book"):
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: "Book"):
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: "Book"):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
