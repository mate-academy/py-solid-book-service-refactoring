import json
import xml.etree.ElementTree as ElemTree
from abc import ABC, abstractmethod


class SerializeBook(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class SerializeBookJSON(SerializeBook):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class SerializeBookXML(SerializeBook):
    def serialize(self, book_title: str, book_content: str) -> str:
        root = ElemTree.Element("book")
        title = ElemTree.SubElement(root, "title")
        title.text = book_title
        content = ElemTree.SubElement(root, "content")
        content.text = book_content
        return ElemTree.tostring(root, encoding="unicode")


BOOK_SERIALIZE_PROCESSORS = {
    "json": SerializeBookJSON,
    "xml": SerializeBookXML,
}
