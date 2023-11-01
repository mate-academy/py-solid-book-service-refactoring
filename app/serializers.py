import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ElementTree


class BaseSerializer(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    @abstractmethod
    def serialize(self) -> None:
        pass


class JsonSerializer(BaseSerializer):
    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class XmlSerializer(BaseSerializer):
    def serialize(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")
