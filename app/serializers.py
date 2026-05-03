import json
import xml.etree.ElementTree as Et

from app.books import Book
from app.interfaces import SerializeBookInterface


class SerializeBookJSON(SerializeBookInterface):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        return json.dumps({
            "title": self.book.title,
            "content": self.book.content
        })


class SerializeBookXML(SerializeBookInterface):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.book.title
        content = Et.SubElement(root, "content")
        content.text = self.book.content
        return Et.tostring(root, encoding="unicode")
