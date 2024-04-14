import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod

from app.model import Book


class BookSerializer(ABC):

    def __init__(self, book: Book) -> None:
        self.book = book
        self.title = self.book.title
        self.content = self.book.content

    @abstractmethod
    def serialize(self) -> str:
        ...


class XMLSerializer(BookSerializer):
    def serialize(self) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.title
        content = Et.SubElement(root, "content")
        content.text = self.content
        return Et.tostring(root, encoding="unicode")


class JSONSerializer(BookSerializer):
    def serialize(self) -> str:
        return json.dumps({
            "title": self.title,
            "content": self.content
        })
