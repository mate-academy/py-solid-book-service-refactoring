import json
import xml.etree.ElementTree as ET  # noqa: N817
from abc import ABC, abstractmethod


class BookInterface(ABC):
    @abstractmethod
    def get_title(self) -> None:
        pass

    @abstractmethod
    def get_content(self) -> None:
        pass


class Book(BookInterface):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def get_title(self) -> str:
        return self.title

    def get_content(self) -> str:
        return self.content


class Command(ABC):
    @abstractmethod
    def execute(self, book: BookInterface) -> None:
        pass


class DisplayConsoleCommand(Command):
    def execute(self, book: BookInterface) -> None:
        print(book.get_content())


class DisplayReverseCommand(Command):
    def execute(self, book: BookInterface) -> None:
        print(book.get_content()[::-1])


class PrintConsoleCommand(Command):
    def execute(self, book: BookInterface) -> None:
        print(f"Printing the book: {book.get_title()}...")
        print(book.get_content())


class PrintReverseCommand(Command):
    def execute(self, book: BookInterface) -> None:
        print(f"Printing the book in reverse: {book.get_title()}...")
        print(book.get_content()[::-1])


class SerializerJSONCommand(Command):
    def execute(self, book: BookInterface) -> str:
        return json.dumps(
            {
                "title": book.get_title(), "content": book.get_content()
            }
        )


class SerializerXMLCommand(Command):
    def execute(self, book: BookInterface) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.get_title()
        content = ET.SubElement(root, "content")
        content.text = book.get_content()
        return ET.tostring(root, encoding="unicode")


class BookService:
    def __init__(self, book: BookInterface, commands: list[Command]) -> None:
        self.book = book
        self.commands = commands

    def execute_all(self) -> list[str | None]:
        results = []
        for command in self.commands:
            result = command.execute(self.book)
            results.append(result)
        return results


def main(
        book: BookInterface,
        commands: list[tuple[str, str | None]]
) -> str | None:
    command_objects: list[Command] = []

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                command_objects.append(DisplayConsoleCommand())
            elif method_type == "reverse":
                command_objects.append(DisplayReverseCommand())
        elif cmd == "print":
            if method_type == "console":
                command_objects.append(PrintConsoleCommand())
            elif method_type == "reverse":
                command_objects.append(PrintReverseCommand())
        elif cmd == "serialize":
            if method_type == "json":
                command_objects.append(SerializerJSONCommand())
            elif method_type == "xml":
                command_objects.append(SerializerXMLCommand())

    service = BookService(book, command_objects)
    results = service.execute_all()
    for output in results:
        if output is not None:
            return output
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    commands = [
        DisplayReverseCommand(),
        SerializerJSONCommand()
    ]
    result = main(sample_book, commands)
    print("Serialize result:", result)
