from abc import ABC, abstractmethod
from app.book import Book
import json
import xml.etree.ElementTree as ElT


class SerializerStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(SerializerStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(SerializerStrategy):
    def serialize(self, book: Book) -> str:
        root = ElT.Element("book")
        title = ElT.SubElement(root, "title")
        title.text = book.title
        content = ElT.SubElement(root, "content")
        content.text = book.content
        return ElT.tostring(root, encoding="unicode")
