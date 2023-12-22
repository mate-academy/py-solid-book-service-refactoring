import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod

from typing import Any


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Any) -> str:
        pass


class SerializeJson(Serialize):
    def serialize(self, book: Any) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml(Serialize):
    def serialize(self, book: Any) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")
