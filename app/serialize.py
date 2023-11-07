from abc import ABC, abstractmethod
import xml.etree.ElementTree as ElementTree
import json

from app.book import Book


class Serialize(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def exec(self) -> str:
        pass


class SerializeJson(Serialize):
    def exec(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class SerializeXml(Serialize):
    def exec(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.book.content
        return ElementTree.tostring(root, encoding="unicode")


serialize_handlers = {
    "json": SerializeJson,
    "xml": SerializeXml
}
