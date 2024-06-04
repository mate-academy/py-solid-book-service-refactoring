import json
import xml.etree.ElementTree as ETree
from abc import ABC, abstractmethod

from app.book import Book


class BaseSerializer(ABC):
    @abstractmethod
    def serialize(self) -> None:
        pass


class JsonSerializer(BaseSerializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class XmlSerializer(BaseSerializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        root = ETree.Element("book")
        title = ETree.SubElement(root, "title")
        title.text = self.book.title
        content = ETree.SubElement(root, "content")
        content.text = self.book.content
        return ETree.tostring(root, encoding="unicode")
