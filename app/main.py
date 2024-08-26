from abc import ABC, abstractmethod
import json
from xml.etree.ElementTree import Element, SubElement, tostring


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


# Implementations for different strategies
class ConsoleDisplayStrategy(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplayStrategy(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


class ConsolePrintStrategy(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrintStrategy(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class JsonSerializeStrategy(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializeStrategy(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = Element("book")
        title_elem = SubElement(root, "title")
        title_elem.text = title
        content_elem = SubElement(root, "content")
        content_elem.text = content
        return tostring(root, encoding="unicode")


# Dependency Inversion: Inject dependencies into the main function
def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategy = {
        "console": ConsoleDisplayStrategy(),
        "reverse": ReverseDisplayStrategy()
    }

    print_strategy = {
        "console": ConsolePrintStrategy(),
        "reverse": ReversePrintStrategy()
    }

    serialize_strategy = {
        "json": JsonSerializeStrategy(),
        "xml": XmlSerializeStrategy()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            display_strategy[method_type].display(book.content)
        elif cmd == "print":
            print_strategy[method_type].print_book(book.title, book.content)
        elif cmd == "serialize":
            return (serialize_strategy[method_type].
                    serialize(book.title, book.content))


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
