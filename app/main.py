from app.display import (
    DisplayType,
    ConsoleDisplayType,
    ReverseDisplayType
)
from app.serialize import (
    SerializeType,
    JsonSerialize,
    XmlSerialize
)
from app.print_book import (
    PrintType,
    PrintConsoleType,
    PrintDisplayType
)


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: DisplayType) -> None:
        display_type.display(self.content)

    def print_book(self, print_type: PrintType) -> None:
        print_type.print_book(self.title, self.content)

    def serialize(self, serializer: SerializeType) -> str:
        return serializer.serialize(self.title, self.content)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:

        if cmd == "display":
            if method_type == "console":
                book.display(ConsoleDisplayType())
            elif method_type == "reverse":
                book.display(ReverseDisplayType())
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            if method_type == "console":
                book.print_book(PrintConsoleType())
            elif method_type == "reverse":
                book.print_book(PrintDisplayType())
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            if method_type == "json":
                return book.serialize(JsonSerialize())
            elif method_type == "xml":
                return book.serialize(XmlSerialize())
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
