import json
import xml.etree.ElementTree as ET  # noqa: N817
from abc import ABC, abstractmethod


# 1. Класс только для хранения данных
class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


# 2. Стратегии форматирования (Open/Closed Principle)
class ContentFormatter(ABC):
    @abstractmethod
    def format(self, content: str) -> str:
        pass


class ConsoleFormatter(ContentFormatter):
    def format(self, content: str) -> str:
        return content


class ReverseFormatter(ContentFormatter):
    def format(self, content: str) -> str:
        return content[::-1]


# 3. Класс для отображения (SRP: только вывод)
class BookDisplay:
    def __init__(self, formatter: ContentFormatter) -> None:
        self.formatter = formatter

    def display(self, book: Book) -> None:
        formatted_content = self.formatter.format(book.content)
        print(formatted_content)


# 4. Класс для печати с заголовком
class BookPrinter:
    def __init__(self) -> None:
        pass

    def print_book(self, book: Book, formatter: ContentFormatter) -> None:
        formatted_content = formatter.format(book.content)
        prefix = (
            " in reverse"
            if isinstance(formatter, ReverseFormatter)
            else ""
        )
        print(f"Printing the book{prefix}: {book.title}...")
        print(formatted_content)


# 5. Стратегии сериализации
class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        ET.SubElement(root, "title").text = book.title
        ET.SubElement(root, "content").text = book.content
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            + ET.tostring(root, encoding="unicode")
        )


# 6. Функция main теперь только координирует
def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    result = None

    for cmd, method_type in commands:
        if cmd == "display":
            # Выбираем форматтер по типу
            formatter = (
                ConsoleFormatter()
                if method_type == "console"
                else ReverseFormatter()
            )
            display = BookDisplay(formatter)
            display.display(book)
            # Возвращаем для теста
            result = formatter.format(book.content)

        elif cmd == "print":
            formatter = (
                ConsoleFormatter()
                if method_type == "console"
                else ReverseFormatter()
            )
            printer = BookPrinter()
            printer.print_book(book, formatter)

        elif cmd == "serialize":
            serializer = (
                JSONSerializer()
                if method_type == "json"
                else XMLSerializer()
            )
            result = serializer.serialize(book)

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
