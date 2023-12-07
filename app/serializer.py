import json
from abc import ABC, abstractmethod
from app.book import Book
import xml.etree.ElementTree as ElemTree


class Serializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.contend}
        )


class XmlSerializer(Serializer):
    def serialize(self) -> str:
        root = ElemTree.Element("book")
        title = ElemTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElemTree.SubElement(root, "content")
        content.text = self.book.contend
        return ElemTree.tostring(root, encoding="unicode")
