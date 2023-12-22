import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self) -> None:
        pass


class JSONSerializer(Serializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> json:
        return json.dumps(
            {
                "title": self.book.title,
                "content": self.book.content
            }
        )


class XMLSerializer(Serializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> Et:
        root = Et.Element("book")

        title = Et.SubElement(root, "title")
        title.text = self.book.title

        content = Et.SubElement(root, "content")
        content.text = self.book.content

        return Et.tostring(root, encoding="unicode")
