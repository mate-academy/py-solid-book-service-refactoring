import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod


class Serialize(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JSONSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        root = Et.Element("book")
        Et.SubElement(root, "title").text = title
        Et.SubElement(root, "content").text = content
        return Et.tostring(root, encoding="unicode")
