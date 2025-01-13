from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = xml.etree.ElementTree.Element("title")
        title_elem = xml.etree.ElementTree.SubElement(root, "title")
        title_elem.text = title
        content_elem = xml.etree.ElementTree.SubElement(root, "content")
        content_elem.text = content
        return xml.etree.ElementTree.tostring(root, encoding="unicode")
