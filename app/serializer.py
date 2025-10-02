import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree

from app.book import IBook


class ISerializer(ABC):
    @abstractmethod
    def serialize(self, book: IBook) -> str:
        pass


class JSONSerializer(ISerializer):
    def serialize(self, book: IBook) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(ISerializer):
    def serialize(self, book: IBook) -> str:
        root = ElementTree.Element("book")
        ElementTree.SubElement(root, "title").text = book.title
        ElementTree.SubElement(root, "content").text = book.content
        return ElementTree.tostring(root, encoding="unicode")
