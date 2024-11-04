import json
import xml.etree.ElementTree as ElementTree
from typing import Optional, List, Tuple


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def _display_content(self, mode: str) -> str:
        if mode == "console":
            return self.content
        elif mode == "reverse":
            return self.content[::-1]
        else:
            raise ValueError(f"Unknown display type: {mode}")

    def display(self, display_type: str, prefix: str = "") -> None:
        content = self._display_content(display_type)
        print(f"{prefix}{content}")

    def print_book(self, print_type: str) -> None:
        self.display(
            print_type,
            prefix=f"Printing the book: {self.title}...\n"
        )

    def _serialize_to_json(self) -> str:
        return json.dumps(
            {"title": self.title,
             "content": self.content}
        )

    def _serialize_to_xml(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")

    def serialize(self, serialize_type: str) -> str:
        serializers = {
            "json": self._serialize_to_json,
            "xml": self._serialize_to_xml
        }
        if serialize_type not in serializers:
            raise ValueError(
                f"Unknown serialize type: {serialize_type}"
            )

        return serializers[serialize_type]()


def main(
        book: Book,
        commands: List[Tuple[str, str]]
) -> Optional[str]:
    actions = {
        "display": book.display,
        "print": book.print_book,
        "serialize": book.serialize,
    }

    result = None
    for cmd, method_type in commands:
        if cmd in actions:
            action = actions[cmd]
            if cmd == "serialize":
                result = action(method_type)
            else:
                action(method_type)
        else:
            raise ValueError(f"Unknown command: {cmd}")
        return result


if __name__ == "__main__":
    sample_book = Book(
        "Sample Book",
        "This is some sample content."
    )
    print(main(
        sample_book,
        [("display", "reverse"),
         ("serialize", "xml")]
    ))
