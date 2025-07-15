from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET

from app.book.book import Book


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book):
        pass


class SerializeJson(Serialize):
    def serialize(self, book: Book):
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml(Serialize):
    def serialize(self, book: Book):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")