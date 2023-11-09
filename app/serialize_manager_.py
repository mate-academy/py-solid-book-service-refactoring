import json
import xml.etree.ElementTree as ElemTree
from abc import ABC, abstractmethod

from app.book import Book


class SerializeBook(ABC):
    method_type = None

    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize_book(self) -> None:
        pass


class SerializeJson(SerializeBook):
    method_type = "json"

    def serialize_book(self) -> str:
        return json.dumps({"title": self.book.title, "content": self.book.content})


class SerializeXML(SerializeBook):
    method_type = "xml"

    def serialize_book(self) -> str:
        root = ElemTree.Element("book")
        title = ElemTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElemTree.SubElement(root, "content")
        content.text = self.book.content
        return ElemTree.tostring(root, encoding="unicode")


def serialize_manager(method: str, book: Book) -> None | str:
    for subclass in SerializeBook.__subclasses__():
        if subclass.method_type == method:
            selected_class = subclass(book=book)
            if selected_class is None:
                raise ValueError(f"Unknown serialize type: {method}")
            return selected_class.serialize_book()
