import json
import xml.etree.ElementTree
from abc import ABC, abstractmethod
from typing import Any


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Any) -> str:
        pass


class SerializeJSON(Serialize):
    def serialize(self, book: Any) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXML(Serialize):
    def serialize(self, book: Any) -> str:
        root = xml.etree.ElementTree.Element("book")
        title = xml.etree.ElementTree.SubElement(root, "title")
        title.text = book.title
        content = xml.etree.ElementTree.SubElement(root, "content")
        content.text = book.content
        return xml.etree.ElementTree.tostring(root, encoding="unicode")
