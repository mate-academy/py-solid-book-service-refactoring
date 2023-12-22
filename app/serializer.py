import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book) -> str:
        pass


class SerializeJson(Serialize):
    def serialize(self, book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml(Serialize):
    def serialize(self, book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
