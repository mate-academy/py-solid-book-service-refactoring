from abc import ABC, abstractmethod
import json
from xml.etree import ElementTree


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class XmlSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")
        title_el = ElementTree.SubElement(root, "title")
        title_el.text = title
        content_el = ElementTree.SubElement(root, "content")
        content_el.text = content
        return ElementTree.tostring(root, encoding="unicode")


class JsonSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})
