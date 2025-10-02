from __future__ import annotations
import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree

from app.book import Book


class ISerializer(ABC):
    _registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        ISerializer._registry[cls.__name__.lower()] = cls

    @classmethod
    def get_serializer(cls, method_type) -> ISerializer:
        if method_type not in ISerializer._registry:
            raise ValueError(f"Unknown serialize type: {method_type}")
        return ISerializer._registry[method_type]()

    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSON(ISerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XML(ISerializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
