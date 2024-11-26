import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ElementTree


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book: str) -> str:
        pass


class JsonSerialize(SerializeStrategy):
    def serialize(self, book: str) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerialize(SerializeStrategy):
    def serialize(self, book: str) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
