import json
import xml.etree.ElementTree as ElTree
from abc import ABC, abstractmethod


class BaseSerializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializer(BaseSerializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(BaseSerializer):
    def serialize(self, title: str, content: str) -> str:
        root = ElTree.Element("book")
        title_elem = ElTree.SubElement(root, "title")
        title_elem.text = title
        content_elem = ElTree.SubElement(root, "content")
        content_elem.text = content
        return ElTree.tostring(root, encoding="unicode")
