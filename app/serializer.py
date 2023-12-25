import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod
from app.book import Book


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> None:
        pass


class SerializerJSON(Serializer):
    @staticmethod
    def serialize(book: Book) -> json:
        return json.dumps(
            {"title": book.title, "content": book.content}
        )


class SerializerXML(Serializer):
    @staticmethod
    def serialize(book: Book) -> Et:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")
