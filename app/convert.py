import json
import xml.etree.ElementTree as ElementTree


class ConvertJSON:
    @staticmethod
    def serialize(title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})

    def __call__(self, *args, **kwargs) -> str:
        return self.serialize(*args, **kwargs)


class ConvertXML:
    @staticmethod
    def serialize(book_title: str, book_content: str) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book_title
        content = ElementTree.SubElement(root, "content")
        content.text = book_content
        return ElementTree.tostring(root, encoding="unicode")

    def __call__(self, *args, **kwargs) -> str:
        return self.serialize(*args, **kwargs)
