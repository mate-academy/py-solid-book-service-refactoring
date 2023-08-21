import json
import xml.etree.ElementTree as El
from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass


class JsonSerializer(Serializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class XmlSerializer(Serializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        root = El.Element("book")
        title = El.SubElement(root, "title")
        title.text = self.book.title
        content = El.SubElement(root, "content")
        content.text = self.book.content
        return El.tostring(root, encoding="unicode")
