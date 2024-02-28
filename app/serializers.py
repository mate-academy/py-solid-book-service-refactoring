import json
import xml.etree.ElementTree as ETree
from abc import ABC, abstractmethod


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        root = ETree.Element("book")
        title_elem = ETree.SubElement(root, "title")
        title_elem.text = title
        content_elem = ETree.SubElement(root, "content")
        content_elem.text = content
        return ETree.tostring(root, encoding="unicode")
