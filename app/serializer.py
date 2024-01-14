import json
from abc import ABC, abstractmethod

from app.books import Book
import xml.etree.ElementTree as Et


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
        return json.dumps(
            {"title": self.title, "content": self.content}
        )


class XmlSerializer(Serializer):
    def __init__(self, book: Book) -> None:
        super().__init__(book)

    def serialize(self) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.title
        content = Et.SubElement(root, "content")
        content.text = self.content
        return Et.tostring(root, encoding="unicode")
