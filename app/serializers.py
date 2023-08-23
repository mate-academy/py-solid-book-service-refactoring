import json
from abc import abstractmethod
import xml.etree.ElementTree as ElementTree

from app.book import Book


class Serializer:
    @abstractmethod
    def perform_serialize(self, book: Book) -> None:
        pass


class SerializerJSON(Serializer):
    def perform_serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializerXML(Serializer):
    def perform_serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
