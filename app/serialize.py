import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod

from app.book import Book


class Serialize(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> str:
        pass


class JSONSerialize(Serialize):
    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class XMLSerialize(Serialize):
    def serialize(self) -> str:
        root = Et.Element("book")
        Et.SubElement(root, "title").text = self.book.title
        Et.SubElement(root, "content").text = self.book.content
        return Et.tostring(root, encoding="unicode")
