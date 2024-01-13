import json
from abc import ABC, abstractmethod

from app.books import Book
import xml.etree.ElementTree as ET


class Serializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> None:
        pass


class JsonSerializer(Serializer):
    def __init__(self, book: Book) -> None:
        super().__init__(book)

    def serialize(self) -> json:
        return json.dumps({"title": self.book.title, "content": self.book.content})


class XmlSerializer(Serializer):
    def __init__(self, book: Book) -> None:
        super().__init__(book)

    def serialize(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")
