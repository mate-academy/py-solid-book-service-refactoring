from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ElementTree
from app.book import Book


class SerializeBook(ABC):
    @abstractmethod
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> str:
        pass


class JsonSerializerBook(SerializeBook):
    def __init__(self, book: Book) -> None:
        super().__init__(book)

    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class XMLSerializerBook(SerializeBook):
    def __init__(self, book: Book) -> None:
        super().__init__(book)

    def serialize(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.book.content
        return ElementTree.tostring(root, encoding="unicode")
