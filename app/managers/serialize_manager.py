import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod
from typing import Optional


class SerializationManager(ABC):
    def __init__(self) -> None:
        self.title: Optional[str] = None
        self.content: Optional[str] = None

    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        self.title = title
        self.content = content


class SerializeJSON(SerializationManager):
    def __init__(self) -> None:
        super().__init__()

    def serialize(self, title: str, content: str) -> str:
        super().serialize(title, content)
        return json.dumps({"title": self.title, "content": self.content})


class SerializeXML(SerializationManager):
    def __init__(self) -> None:
        super().__init__()

    def serialize(self, title: str, content: str) -> str:
        super().serialize(title, content)
        root = ElementTree.Element("book")
        title_elem = ElementTree.SubElement(root, "title")
        title_elem.text = self.title
        content_elem = ElementTree.SubElement(root, "content")
        content_elem.text = self.content
        return ElementTree.tostring(root, encoding="unicode")
