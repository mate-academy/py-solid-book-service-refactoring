import json
import xml.etree.ElementTree as xml_ET
from dataclasses import asdict
from abc import ABC, abstractmethod

from app.book import Book


class BaseSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(BaseSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps(asdict(book))


class XmlSerializer(BaseSerializer):
    def serialize(self, book: Book) -> str:
        root = xml_ET.Element("book")
        for element, text in asdict(book).items():
            sub_element = xml_ET.SubElement(root, element)
            sub_element.text = text
        return xml_ET.tostring(root, encoding="unicode")


class Serializer:
    def __init__(self, serializer: BaseSerializer) -> None:
        self._serializer = serializer

    def serialize(self, book: Book) -> str:
        return self._serializer.serialize(book)
