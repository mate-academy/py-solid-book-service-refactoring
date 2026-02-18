import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ElementTree


class Serializer(ABC):
    @abstractmethod
    def serialize(self, name: str, text: str) -> None | str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, name: str, text: str) -> None | str:
        return json.dumps({"title": name, "content": text})


class XMLSerializer(Serializer):
    def serialize(self, name: str, text: str) -> None | str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = name
        content = ElementTree.SubElement(root, "content")
        content.text = text
        return ElementTree.tostring(root, encoding="unicode")
