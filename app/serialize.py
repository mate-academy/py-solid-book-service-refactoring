import json
import xml.etree.ElementTree as ET  # noqa
from abc import ABC, abstractmethod


class SerializeType(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerialize(SerializeType):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(SerializeType):
    def serialize(self, title: str, content: str) -> str:
        root = ET.Element("book")
        titl = ET.SubElement(root, "title")
        titl.text = title
        content_ = ET.SubElement(root, "content")
        content_.text = content
        return ET.tostring(root, encoding="unicode")
