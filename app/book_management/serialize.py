import json
from xml.etree import ElementTree

from abc import ABC, abstractmethod


class Serialize(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> None:
        raise ValueError("Unknown serialize type")


class JsonSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")
        title_info = ElementTree.SubElement(root, "title")
        title_info.text = title
        content_info = ElementTree.SubElement(root, "content")
        content_info.text = content
        return ElementTree.tostring(root, encoding="unicode")
