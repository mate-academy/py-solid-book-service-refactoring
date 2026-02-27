import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from app.models import Book

class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass

class ConsoleFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content

class ReverseFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content[::-1]

class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass

class JSONSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

class XMLSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
