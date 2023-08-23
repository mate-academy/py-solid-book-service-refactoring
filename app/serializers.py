import json
import xml.etree.ElementTree as ElTree
from abc import ABC, abstractmethod

from app.book import Book


class BaseSerializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> None:
        pass


class JSONSerializer(BaseSerializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(BaseSerializer):
    @staticmethod
    def serialize(book: Book) -> None:
        root = ElTree.Element("book")
        title = ElTree.SubElement(root, "title")
        title.text = book.title
        content = ElTree.SubElement(root, "content")
        content.text = book.content
        return ElTree.tostring(root, encoding="unicode")
