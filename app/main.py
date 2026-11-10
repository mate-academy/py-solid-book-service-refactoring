import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class ConsolePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")
        title_el = ElementTree.SubElement(root, "title")
        title_el.text = title
        content_el = ElementTree.SubElement(root, "content")
        content_el.text = content
        return ElementTree.tostring(root, encoding="unicode")


DISPLAY_STRATEGIES: dict[str, DisplayStrategy] = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_STRATEGIES: dict[str, PrintStrategy] = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}

SERIALIZE_STRATEGIES: dict[str, SerializeStrategy] = {
    "json": JsonSerialize(),
    "xml": XmlSerialize(),
}


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        strategy = DISPLAY_STRATEGIES.get(display_type)
        if strategy is None:
            raise ValueError(f"Unknown display type: {display_type}")
        strategy.display(self.content)

    def print_book(self, print_type: str) -> None:
        strategy = PRINT_STRATEGIES.get(print_type)
        if strategy is None:
            raise ValueError(f"Unknown print type: {print_type}")
        strategy.print_book(self.title, self.content)

    def serialize(self, serialize_type: str) -> str:
        strategy = SERIALIZE_STRATEGIES.get(serialize_type)
        if strategy is None:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return strategy.serialize(self.title, self.content)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
