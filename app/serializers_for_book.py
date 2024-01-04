import json
from xml.etree import ElementTree

from abc import ABC, abstractmethod

from app.book_class import Book


class SerializeStrategy(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> str:
        pass


class JsonSerialize(SerializeStrategy):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialize(SerializeStrategy):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ElementTree.Element("book")
        title_element = ElementTree.SubElement(root, "title")
        title_element.text = book.title
        content_element = ElementTree.SubElement(root, "content")
        content_element.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
