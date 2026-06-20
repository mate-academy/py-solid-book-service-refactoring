from __future__ import annotations
from abc import ABC, abstractmethod
import json
from xml.etree import ElementTree


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        raise NotImplementedError


class JSONSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")
        title_el = ElementTree.SubElement(root, "title")
        title_el.text = title
        content_el = ElementTree.SubElement(root, "content")
        content_el.text = content
        return ElementTree.tostring(root, encoding="unicode")


def get_serializer(name: str) -> Serializer:
    mapping: dict[str, Serializer] = {
        "json": JSONSerializer(),
        "xml": XMLSerializer(),
    }
    try:
        return mapping[name]
    except KeyError:
        raise ValueError(f"Unknown serialize type: {name}")
