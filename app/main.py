import json
import xml.etree.ElementTree as ElementTree


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayService:
    @staticmethod
    def display(content: str, display_type: str) -> None:
        if display_type == "console":
            print(content)
        elif display_type == "reverse":
            print(content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class PrintService:
    @staticmethod
    def print_book(title: str, content: str, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {title}...")
            print(content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {title}...")
            print(content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class SerializeService:
    @staticmethod
    def serialize(title: str, content: str, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": title, "content": content})
        elif serialize_type == "xml":
            root = ElementTree.Element("book")
            title_elem = ElementTree.SubElement(root, "title")
            title_elem.text = title
            content_elem = ElementTree.SubElement(root, "content")
            content_elem.text = content
            return ElementTree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DisplayService.display(book.content, method_type)
        elif cmd == "print":
            PrintService.print_book(book.title, book.content, method_type)
        elif cmd == "serialize":
            return SerializeService.serialize(
                book.title,
                book.content,
                method_type
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
