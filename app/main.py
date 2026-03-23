import json
import xml.etree.ElementTree as elementtree


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayService:
    @staticmethod
    def display(book: Book, display_type: str) -> None:
        if display_type == "console":
            print(book.content)
        elif display_type == "reverse":
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class PrintService:
    @staticmethod
    def print_book(book: Book, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class SerializeService:
    @staticmethod
    def serialize(book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({
                "title": book.title,
                "content": book.content,
            })

        if serialize_type == "xml":
            root = elementtree.Element("book")

            title = elementtree.SubElement(root, "title")
            title.text = book.title

            content = elementtree.SubElement(root, "content")
            content.text = book.content

            return elementtree.tostring(root, encoding="unicode")

        raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DisplayService.display(book, method_type)
        elif cmd == "print":
            PrintService.print_book(book, method_type)
        elif cmd == "serialize":
            return SerializeService.serialize(book, method_type)

    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
