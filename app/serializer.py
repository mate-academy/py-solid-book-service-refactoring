import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self) -> None:
        pass


class JsonSerialize(Serializer):
    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class XMLSerialize(Serializer):
    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def serialize(self) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.title
        content = Et.SubElement(root, "content")
        content.text = self.content
        return Et.tostring(root, encoding="unicode")
