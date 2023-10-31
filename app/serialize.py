import json
import xml.etree.ElementTree as ET
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
        root = ET.Element("book")
        ET.SubElement(root, "title").text = title
        ET.SubElement(root, "content").text = content
        return ET.tostring(root, encoding="unicode")
