import json
from xml.etree import ElementTree as elt


class ConvertJson:
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})

    def __call__(self, *args, **kwargs) -> str:
        return self.serialize(*args, **kwargs)


class ConvertXml:
    def serialize(self, book_title: str, book_content: str) -> str:
        root = elt.Element("book")
        title = elt.SubElement(root, "title")
        title.text = book_title
        content = elt.SubElement(root, "content")
        content.text = book_content
        return elt.tostring(root, encoding="unicode")

    def __call__(self, *args, **kwargs) -> str:
        return self.serialize(*args, **kwargs)
