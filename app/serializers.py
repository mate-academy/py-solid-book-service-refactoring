import json
import xml.etree.ElementTree as ETree
from abc import ABC, abstractmethod

from app.protocols import HasTitleAndContent


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(obj: HasTitleAndContent) -> str:
        pass


class JsonSerializer(Serializer):
    @staticmethod
    def serialize(obj: HasTitleAndContent) -> str:
        return json.dumps({"title": obj.title, "content": obj.content})


class BookXmlSerializer(Serializer):
    @staticmethod
    def serialize(obj: HasTitleAndContent) -> str:
        root = ETree.Element("book")
        title = ETree.SubElement(root, "title")
        title.text = obj.title
        content = ETree.SubElement(root, "content")
        content.text = obj.content
        return ETree.tostring(root, encoding="unicode")
