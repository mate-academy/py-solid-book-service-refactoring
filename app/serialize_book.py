import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree


class BaseSerializeBook(ABC):

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    @abstractmethod
    def serialize(self, method_type: str) -> str:
        pass


class XmlSerializeBook(BaseSerializeBook):

    def serialize(self, method_type: str) -> str:
        if method_type == "xml":
            root = ElementTree.Element("book")
            title = ElementTree.SubElement(root, "title")
            title.text = self.title
            content = ElementTree.SubElement(root, "content")
            content.text = self.content
            return ElementTree.tostring(root, encoding="unicode")
        else:
            return super().serialize(method_type)


class JsonSerializeBook(BaseSerializeBook):

    def serialize(self, method_type: str) -> str:
        if method_type == "json":
            return json.dumps({"title": self.title, "content": self.content})
        else:
            return super().serialize(method_type)


class SerializeBook(XmlSerializeBook, JsonSerializeBook):
    pass
