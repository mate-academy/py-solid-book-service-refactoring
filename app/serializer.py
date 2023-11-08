import abc
import json
import xml.etree.ElementTree as ElementTree

from app.book import Book


class SerializeBook(abc.ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abc.abstractmethod
    def serialize(self) -> str:
        pass


class SerializeJson(SerializeBook):

    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class SerializeXml(SerializeBook):
    def serialize(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.book.content
        return ElementTree.tostring(root, encoding="unicode")
