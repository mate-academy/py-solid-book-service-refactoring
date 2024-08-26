import json
from abc import abstractmethod, ABC
from xml.etree.ElementTree import Element, SubElement, tostring

from app.book import Book


class SerializerBase(ABC):
    @abstractmethod
    def serializer(self, book: Book) -> str:
        pass


class JsonSerializer(SerializerBase):
    def serializer(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializerBase):
    def serializer(self, book: Book) -> str:
        root = Element("book")
        title = SubElement(root, "title")
        title.text = book.title
        content = SubElement(root, "content")
        content.text = book.content
        return tostring(root, encoding="unicode")
