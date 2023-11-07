from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ElementTree

from app.book import Book


class BaseSerializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self: Book) -> str:
        pass


class JsonSerializer(BaseSerializer):
    def serialize(self: Book) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class XmlSerializer(BaseSerializer):
    def serialize(self: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")
