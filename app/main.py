import json
import xml.etree.ElementTree as ET  # noqa: N817
from abc import ABC, abstractmethod
from typing import Any


# 1. Класс только для хранения данных
class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


# Абстрактная команда
class Command(ABC):
    @abstractmethod
    def execute(self, book: Book, method_type: str) -> Any:
        pass


class DisplayCommand(Command):
    def execute(self, book: Book, method_type: str) -> str:
        if method_type == "console":
            return book.content
        elif method_type == "reverse":
            return book.content[::-1]
        raise ValueError(f"Unknown display type: {method_type}")


class PrintCommand(Command):
    def execute(self, book: Book, method_type: str) -> None:
        if method_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif method_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {method_type}")


class SerializeCommand(Command):
    def execute(self, book: Book, method_type: str) -> str:
        if method_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif method_type == "xml":
            root = ET.Element("book")
            ET.SubElement(root, "title").text = book.title
            ET.SubElement(root, "content").text = book.content
            return ET.tostring(root, encoding="unicode")
        raise ValueError(f"Unknown serialize type: {method_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    # Словарь команд - легко расширяемый
    command_map = {
        "display": DisplayCommand(),
        "print": PrintCommand(),
        "serialize": SerializeCommand(),
    }

    result = None
    for cmd, method_type in commands:
        if cmd not in command_map:
            raise ValueError(f"Unknown command: {cmd}")

        output = command_map[cmd].execute(book, method_type)

        # Команда display должна выводить результат в консоль
        if cmd == "display":
            print(output)

        # Команда serialize сохраняет результат для возврата
        elif cmd == "serialize":
            result = output

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
