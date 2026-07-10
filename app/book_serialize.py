import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET

from app.book import Book


class SerializerType(ABC):
    @abstractmethod
    def serialize(self, book: Book):
        pass


class SerializerJSON(SerializerType):
    def serialize(self, book: Book):
        return json.dumps({"title": book.title, "content": book.content})


class SerializerXML(SerializerType):
    def serialize(self, book: Book):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
