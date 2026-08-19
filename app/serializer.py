import json
import xml.etree.ElementTree as ETree

from abc import ABC, abstractmethod

from app.book import Book


class SerializerBase(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JsonSerializer(SerializerBase):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializerBase):
    def serialize(self, book: Book) -> str:
        root = ETree.Element("book")

        title = ETree.SubElement(root, "title")
        title.text = book.title

        content = ETree.SubElement(root, "content")
        content.text = book.content

        return ETree.tostring(root, encoding="unicode")
