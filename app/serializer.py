import json
import xml.etree.ElementTree

from abc import ABC, abstractmethod
from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = xml.etree.ElementTree.Element("book")
        xml.etree.ElementTree.SubElement(root, "title").text = book.title
        xml.etree.ElementTree.SubElement(root, "content").text = book.content
        return xml.etree.ElementTree.tostring(root, encoding="unicode")
