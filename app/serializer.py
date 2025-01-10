import json
import xml.etree.ElementTree as ElTree
from abc import abstractmethod, ABC

from app.book import Book


class Serializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self) -> str:
        return json.dumps({
            "title": self.book.title, "content": self.book.content
        })


class XmlSerializer(Serializer):
    def serialize(self) -> str:
        root = ElTree.Element("book")
        title = ElTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElTree.SubElement(root, "content")
        content.text = self.book.content
        return ElTree.tostring(root, encoding="unicode")
