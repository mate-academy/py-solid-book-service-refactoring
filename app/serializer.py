import json
from xml.etree import ElementTree

from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):

    @abstractmethod
    def serialize(self) -> None:
        pass


class JSONSerializer(Serializer):

    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def serialize(self) -> json:
        return json.dumps(
            {
                "title": self.title,
                "content": self.content
            }
        )


class XMLSerializer(Serializer):

    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book

    def serialize(self) -> ElementTree:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")
