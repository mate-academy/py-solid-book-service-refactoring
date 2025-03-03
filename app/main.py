import json
import xml.etree.ElementTree
from abc import ABC, abstractmethod


# Step 1: Define Interfaces (Abstract Base Classes)
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


# Step 2: Implement Concrete Strategies

# Display Strategies
class ConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


# Print Strategies
class ConsolePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(PrintStrategy):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


# Serialize Strategies
class JSONSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = xml.etree.ElementTree.Element("book")
        title_elem = xml.etree.ElementTree.SubElement(root, "title")
        title_elem.text = title
        content_elem = xml.etree.ElementTree.SubElement(root, "content")
        content_elem.text = content
        return xml.etree.ElementTree.tostring(root, encoding="unicode")


# Step 3: Refactor the Book Class to Use the Strategies
class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def set_display_strategy(self, strategy: DisplayStrategy) -> None:
        self.display_strategy = strategy

    def set_print_strategy(self, strategy: PrintStrategy) -> None:
        self.print_strategy = strategy

    def set_serialize_strategy(self, strategy: SerializeStrategy) -> None:
        self.serialize_strategy = strategy

    def display(self) -> None:
        self.display_strategy.display(self.content)

    def print_book(self) -> None:
        self.print_strategy.print_book(self.title, self.content)

    def serialize(self) -> str:
        return self.serialize_strategy.serialize(self.title, self.content)


# Step 4: Refactor the Main Function
def main(book: Book, commands: list[tuple[str, str]]) -> str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                book.set_display_strategy(ConsoleDisplay())
            elif method_type == "reverse":
                book.set_display_strategy(ReverseDisplay())
            book.display()

        elif cmd == "print":
            if method_type == "console":
                book.set_print_strategy(ConsolePrint())
            elif method_type == "reverse":
                book.set_print_strategy(ReversePrint())
            book.print_book()

        elif cmd == "serialize":
            if method_type == "json":
                book.set_serialize_strategy(JSONSerialize())
            elif method_type == "xml":
                book.set_serialize_strategy(XMLSerialize())
            return book.serialize()


# Step 5: Example Usage
if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    commands = [("display", "reverse"), ("serialize", "xml")]
    print(main(sample_book, commands))
