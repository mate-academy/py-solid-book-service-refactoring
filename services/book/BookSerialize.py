import json
import xml.etree.ElementTree as ET

from abc import abstractmethod, ABC


class BookSerialize(ABC):
    # if I use Book, program not working
    def __init__(self, book: any) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> any:
        pass


class BookSerializeJson(BookSerialize):
    def serialize(self) -> any:
        return json.dumps({
            "title": self.book.title,
            "content": self.book.content
        })


class BookSerializeXML(BookSerialize):
    def serialize(self) -> any:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")
