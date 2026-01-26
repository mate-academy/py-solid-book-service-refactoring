import xml.etree.ElementTree as eT
import json
from abc import ABC, abstractmethod
from app.interfaces import HasTitleContent


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book: HasTitleContent) -> str:
        pass


class JsonSerializer(SerializeStrategy):
    def serialize(self, book: HasTitleContent) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializeStrategy):
    def serialize(self, book: HasTitleContent) -> str:
        root = eT.Element("book")

        title = eT.SubElement(root, "title")
        title.text = book.title

        content = eT.SubElement(root, "content")
        content.text = book.content

        return eT.tostring(root, encoding="unicode")
