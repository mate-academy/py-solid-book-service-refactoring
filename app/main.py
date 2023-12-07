import json
import xml.etree.ElementTree as ElemTree


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display_console(self) -> None:
        print(self.content)

    def display_reverse(self) -> None:
        print(self.content[::-1])

    def print_console(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def print_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])

    def serialize_to_json(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})

    def serialize_to_xml(self) -> str:
        root = ElemTree.Element("book")
        title = ElemTree.SubElement(root, "title")
        title.text = self.title
        content = ElemTree.SubElement(root, "content")
        content.text = self.content
        return ElemTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            (
                book.display_reverse() if method_type == "reverse"
                else book.display_console()
            )
        elif cmd == "print":
            (
                book.print_reverse() if method_type == "reverse"
                else book.print_console()
            )
        elif cmd == "serialize":
            return (
                book.serialize_to_json() if method_type == "json"
                else book.serialize_to_xml()
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
