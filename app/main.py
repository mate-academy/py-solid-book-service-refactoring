from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book):
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, book):
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book):
        print(book.content[::-1])


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, book):
        pass


class ConsolePrint(PrintStrategy):
    def print_book(self, book):
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    def print_book(self, book):
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book):
        pass


class JsonSerializer(SerializeStrategy):
    def serialize(self, book):
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializeStrategy):
    def serialize(self, book):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class Book:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self, strategy: DisplayStrategy):
        strategy.display(self)

    def print_book(self, strategy: PrintStrategy):
        strategy.print_book(self)

    def serialize(self, strategy: SerializeStrategy):
        return strategy.serialize(self)


def get_display_strategy(display_type):
    if display_type == "console":
        return ConsoleDisplay()
    elif display_type == "reverse":
        return ReverseDisplay()
    else:
        raise ValueError(f"Unknown display type: {display_type}")


def get_print_strategy(print_type):
    if print_type == "console":
        return ConsolePrint()
    elif print_type == "reverse":
        return ReversePrint()
    else:
        raise ValueError(f"Unknown print type: {print_type}")


def get_serialize_strategy(serialize_type):
    if serialize_type == "json":
        return JsonSerializer()
    elif serialize_type == "xml":
        return XmlSerializer()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = get_display_strategy(method_type)
            book.display(strategy)
        elif cmd == "print":
            strategy = get_print_strategy(method_type)
            book.print_book(strategy)
        elif cmd == "serialize":
            strategy = get_serialize_strategy(method_type)
            return book.serialize(strategy)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
