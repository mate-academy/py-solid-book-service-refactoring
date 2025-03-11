import json
import xml.etree.ElementTree as ElemTree
from abc import ABC, abstractmethod
from app.book import Book


class SerializationStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerialization(SerializationStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialization(SerializationStrategy):
    def serialize(self, book: Book) -> str:
        root = ElemTree.Element("book")
        title = ElemTree.SubElement(root, "title")
        title.text = book.title
        content = ElemTree.SubElement(root, "content")
        content.text = book.content
        return ElemTree.tostring(root, encoding="unicode")
