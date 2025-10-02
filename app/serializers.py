import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from app.books import Book

class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JsonBookSerializer(BookSerializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self, book: Book) -> str:
        return json.dumps({"title": self.book.title, "content": self.book.content})


class XmlBookSerializer(BookSerializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")
