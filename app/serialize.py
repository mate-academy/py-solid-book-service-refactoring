import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod


class Serialize(ABC):
    @abstractmethod
    def saving_method(self, title: str, content: str) -> str:
        pass


class JsonSerialize(Serialize):
    def saving_method(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(Serialize):
    def saving_method(self, title: str, content: str) -> str:
        root = Et.Element("book")
        Et.SubElement(root, "title").text = title
        Et.SubElement(root, "content").text = content
        return Et.tostring(root, encoding="unicode")
