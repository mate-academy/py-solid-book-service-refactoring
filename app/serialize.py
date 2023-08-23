import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod

from app.book import Book


class SerializeBase(ABC):
    @abstractmethod
    def get_serialize(self, book: Book, serialize_type: str) -> str:
        pass

    @abstractmethod
    def serialize_xml(self, book: Book) -> str:
        pass

    @abstractmethod
    def serialize_json(self, book: Book) -> str:
        pass


class Serialize(SerializeBase):

    def get_serialize(self, book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return self.serialize_json(book)
        elif serialize_type == "xml":
            return self.serialize_xml(book)
        else:
            raise ValueError(f"Неизвестный тип сериализации: {serialize_type}")

    def serialize_xml(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")

    def serialize_json(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})
