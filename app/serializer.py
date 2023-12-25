import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from app.book import Book


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> None:
        pass


class SerializerJSON(Serializer):
    @staticmethod
    def serialize(book: Book) -> json:
        return json.dumps(
            {"title": book.title, "content": book.content}
        )


class SerializerXML(Serializer):
    @staticmethod
    def serialize(book: Book) -> ET:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
