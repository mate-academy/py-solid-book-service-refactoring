import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree


class Serializer(ABC):
    @abstractmethod
    def serialize(self, name: str, title_: str, content_: str) -> str:
        pass


class XmlSerializer(Serializer):
    def serialize(self, name: str, title_: str, content_: str) -> str:
        root = ElementTree.Element(name)
        title = ElementTree.SubElement(root, "title")
        title.text = title_
        content = ElementTree.SubElement(root, "content")
        content.text = content_
        return ElementTree.tostring(root, encoding="unicode")


class JsonSerializer(Serializer):
    def serialize(self, name: str, title_: str, content_: str) -> str:
        return json.dumps({"title": title_, "content": content_})
