from app.book_service import BookService
import json
import xml.etree.ElementTree as Element_tree


class SerializeService(BookService):
    def execute(self, method_type: str) -> None | str:
        if method_type == "json":
            return json.dumps({
                "title": self.book.title,
                "content": self.book.content
            })
        elif method_type == "xml":
            root = Element_tree.Element("book")
            title = Element_tree.SubElement(root, "title")
            title.text = self.book.title
            content = Element_tree.SubElement(root, "content")
            content.text = self.book.content
            return Element_tree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {method_type}")
