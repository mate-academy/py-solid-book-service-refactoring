import json
import xml.etree.ElementTree as Et


class ConvertJson:
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})

    def __call__(self, *args, **kwargs) -> str:
        return self.serialize(*args, **kwargs)


class ConvertXml:
    def serialize(self, book_title: str, book_content: str) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book_title
        content = Et.SubElement(root, "content")
        content.text = book_content
        return Et.tostring(root, encoding="unicode")

    def __call__(self, *args, **kwargs) -> str:
        return self.serialize(*args, **kwargs)
