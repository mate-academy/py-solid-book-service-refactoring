import json
import xml.etree.ElementTree as ETree


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Command:
    def __init__(self, command_name: str, command_type: str) -> None:
        self.command_name = command_name
        self.command_type = command_type

    def display(self, book: Book) -> None:
        if self.command_type == "console":
            print(book.content)
        elif self.command_type == "reverse":
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {self.command_type}")

    def print_book(self, book: Book) -> None:
        if self.command_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif self.command_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {self.command_type}")

    def serialize(self, book: Book) -> str:
        if self.command_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif self.command_type == "xml":
            root = ETree.Element("book")
            title = ETree.SubElement(root, "title")
            title.text = book.title
            content = ETree.SubElement(root, "content")
            content.text = book.content
            return ETree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {self.command_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        command = Command(cmd, method_type)
        if cmd == "display":
            command.display(book)
        elif cmd == "print":
            command.print_book(book)
        elif cmd == "serialize":
            return command.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
