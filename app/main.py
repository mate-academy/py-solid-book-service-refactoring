import json
import xml.etree.ElementTree as ET  # noqa: N817
from enum import Enum
from typing import Optional


class DisplayType(Enum):
    CONSOLE = "console"
    REVERSE = "reverse"


class SerializeType(Enum):
    JSON = "json"
    XML = "xml"


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def _get_formatted_content(self, display_type: DisplayType) -> str:
        if display_type == DisplayType.REVERSE:
            return self.content[::-1]
        return self.content

    def display(
        self, display_type: DisplayType
    ) -> None:
        """Выводит содержимое книги в указанный поток."""
        print(self._get_formatted_content(display_type))

    def print_book(
        self, display_type: DisplayType
    ) -> None:
        """Печатает служебное сообщение и содержимое книги."""
        prefix = " in reverse" if display_type == DisplayType.REVERSE else ""
        print(f"Printing the book{prefix}: {self.title}...")
        self.display(display_type)

    def serialize(self, serialize_type: SerializeType) -> str:
        if serialize_type == SerializeType.JSON:
            return json.dumps({"title": self.title, "content": self.content})
        elif serialize_type == SerializeType.XML:
            root = ET.Element("book")
            ET.SubElement(root, "title").text = self.title
            ET.SubElement(root, "content").text = self.content
            # Добавляем XML-декларацию
            # tree = ET.ElementTree(root)
            return (
                '<?xml version="1.0" encoding="UTF-8"?>\n'
                + ET.tostring(root, encoding="unicode")
            )
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(
    book: Book, commands: list[tuple[str, str]]
) -> Optional[str]:
    """
    Выполняет последовательность команд над книгой.
    Возвращает результат последней команды serialize или None.
    """
    last_serialize = None
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(DisplayType(method_type))
        elif cmd == "print":
            book.print_book(DisplayType(method_type))
        elif cmd == "serialize":
            last_serialize = book.serialize(SerializeType(method_type))
        else:
            raise ValueError(f"Unknown command: {cmd}")
    return last_serialize


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
