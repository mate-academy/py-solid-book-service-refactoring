import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as Tree


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> None:
        pass


class JsonSerializeStrategy(SerializeStrategy):
    def serialize(self, title: str, content: str) -> None:
        return json.dumps({"title": title, "content": content})


class XmlSerializeStrategy(SerializeStrategy):
    def serialize(self, title: str, content: str) -> None:
        root = Tree.Element("book")
        title_elem = Tree.SubElement(root, "title")
        title_elem.text = title
        content_elem = Tree.SubElement(root, "content")
        content_elem.text = content
        return Tree.tostring(root, encoding="unicode")
