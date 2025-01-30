import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        pass

    def print(self, print_type: str) -> None:
        pass

    def serialize(self, serializer_type: str) -> None:
        pass


class BookDisplay(Book):

    def display(self, display_type: str) -> None:
        if display_type == "console":
            print(self.content)
        elif display_type == "reverse":
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class BookPrint(Book):

    def print(self, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {self.title}...")
            print(self.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {self.title}...")
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class BookSerializer(Book):

    def serialize(self, serializer_type: str) -> str:
        if serializer_type == "json":
            return json.dumps({"title": self.title, "content": self.content})
        elif serializer_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = self.title
            content = ET.SubElement(root, "content")
            content.text = self.content
            return ET.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serializer_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            BookDisplay(title=book.title, content=book.content).display(
                display_type=method_type
            )
        elif cmd == "print":
            BookPrint(title=book.title, content=book.content).print(
                print_type=method_type
            )
        elif cmd == "serialize":
            return BookSerializer(
                title=book.title,
                content=book.content
            ).serialize(
                serializer_type=method_type
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
