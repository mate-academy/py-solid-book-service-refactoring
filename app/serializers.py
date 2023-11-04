import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as eT

from app.book import Book


class Serializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @property
    @abstractmethod
    def data(self) -> str:
        ...


class JSONBookSerializer(Serializer):
    @property
    def data(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class XMLBookSerializer(Serializer):
    @property
    def data(self) -> str:
        root = eT.Element("book")
        title = eT.SubElement(root, "title")
        title.text = self.book.title
        content = eT.SubElement(root, "content")
        content.text = self.book.content
        return eT.tostring(root, encoding="unicode")
