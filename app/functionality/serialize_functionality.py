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
    serialize_types = {
        "json": SerializeJsonBook,
        "xml": SerializeXmlBook,
    }
    if serialize_type in serialize_types:
        serialize_class = serialize_types.get(serialize_type)
        return serialize_class(title=title, content=content).serialize_book()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")

