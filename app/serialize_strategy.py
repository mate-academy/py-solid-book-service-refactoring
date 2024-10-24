import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod

from app.book import Book


class SerializeStrategy(ABC):

    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JsonSerializeStrategy(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializeStrategy(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        result = ElementTree.tostring(root, encoding="unicode")
        return result


class SerializeStrategyHandler:
    def __init__(
            self,
            serialize_json: SerializeStrategy,
            serialize_xml: SerializeStrategy
    ) -> None:
        self.serialize_json = serialize_json
        self.serialize_xml = serialize_xml

    def serialize(self, book: Book, serialize_type: str) -> None:
        if serialize_type == "json":
            return self.serialize_json.serialize(book)
        elif serialize_type == "xml":
            return self.serialize_xml.serialize(book)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
