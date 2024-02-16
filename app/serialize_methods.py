import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod


class SerializeMethod(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerialize(SerializeMethod):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(SerializeMethod):
    def serialize(self, title: str, content: str) -> str:
        root = Et.Element("book")
        title_elem = Et.SubElement(root, "title")
        title_elem.text = title
        content_elem = Et.SubElement(root, "content")
        content_elem.text = content
        return Et.tostring(root, encoding="unicode")
