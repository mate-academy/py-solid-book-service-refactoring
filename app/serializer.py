import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from app.book import Book


class SerializerStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(SerializerStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps(
            {
                "title": book.title,
                "content": book.content,
            }
        )


class XmlSerializer(SerializerStrategy):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")

        title_element = ET.SubElement(root, "title")
        title_element.text = book.title

        content_element = ET.SubElement(root, "content")
        content_element.text = book.content

        return ET.tostring(root, encoding="unicode")
