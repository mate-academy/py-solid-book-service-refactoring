import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class SerializeProcessor(ABC):

    @staticmethod
    @abstractmethod
    def serialize(title: str, content: str) -> str:
        pass


class JSONSerializeProcessor(SerializeProcessor):

    @staticmethod
    def serialize(title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerializeProcessor(SerializeProcessor):

    @staticmethod
    def serialize(title: str, content: str) -> str:
        root = ElementTree.Element("book_service")
        title_xml = ElementTree.SubElement(root, "title")
        title_xml.text = title
        content_xml = ElementTree.SubElement(root, "content")
        content_xml.text = content
        return ElementTree.tostring(root, encoding="unicode")
