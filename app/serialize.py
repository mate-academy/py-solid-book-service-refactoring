from abc import ABC, abstractmethod

from app.book import Book
import json
import xml.etree.ElementTree as EleTr


class Serialize(ABC):
    @abstractmethod
    def do_action(self) -> None:
        raise NotImplementedError("Must override this method")


class SerializeJSON(Serialize):
    def __init__(self, book: Book) -> None:
        self.content = book.content
        self.title = book.title

    def do_action(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class SerializeXML(Serialize):
    def __init__(self, book: Book) -> None:
        self.content = book.content
        self.title = book.title

    def do_action(self) -> EleTr:
        root = EleTr.Element("book")
        title = EleTr.SubElement(root, "title")
        title.text = self.title
        content = EleTr.SubElement(root, "content")
        content.text = self.content
        return EleTr.tostring(root, encoding="unicode")
