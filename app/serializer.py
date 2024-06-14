import json

from xml.etree import ElementTree
from abc import ABC, abstractmethod
from app.book import Book


class AbstractBookSerializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> None:
        pass


class JsonSerializer(AbstractBookSerializer):
    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class XmlSerializer(AbstractBookSerializer):
    def serialize(self) -> str:
            root = ElementTree.Element("book")
            title = ElementTree.SubElement(root, "title")
            title.text = self.book.title
            content = ElementTree.SubElement(root, "content")
            content.text = self.book.content
            return ElementTree.tostring(root, encoding="unicode")
