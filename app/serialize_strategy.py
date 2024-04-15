import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod

from app.book import Book


class SerializeStrategy(ABC):

    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerialize(SerializeStrategy):

    def serialize(self, book: Book) -> str:
        return json.dumps(
            {
                "title": book.title,
                "content": book.content,
            }
        )


class XMLSerialize(SerializeStrategy):

    def serialize(self, book: Book) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")
