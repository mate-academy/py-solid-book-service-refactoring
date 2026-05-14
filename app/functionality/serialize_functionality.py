import json
from abc import abstractmethod, ABC
import xml.etree.ElementTree as ET  # noqa: N817


class SerializeBook(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    @abstractmethod
    def serialize_book(self) -> None:
        pass


class SerializeJsonBook(SerializeBook) :
    def serialize_book(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class SerializeXmlBook(SerializeBook):
    def serialize_book(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")


def serialize_book_func(serialize_type: str, title: str, content: str) -> str:
    if serialize_type == "json":
        return SerializeJsonBook(title, content).serialize_book()
    elif serialize_type == "xml":
        return SerializeXmlBook(title, content).serialize_book()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
