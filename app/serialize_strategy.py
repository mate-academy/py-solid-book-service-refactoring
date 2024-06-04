from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as elementTree


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializeStrategy(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializeStrategy(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = elementTree.Element("book")
        title_elem = elementTree.SubElement(root, "title")
        title_elem.text = title
        content_elem = elementTree.SubElement(root, "content")
        content_elem.text = content
        return elementTree.tostring(root, encoding="unicode")
