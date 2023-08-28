from __future__ import annotations

from app.display import ConsoleDisplay, ReversedDisplay
from app.print import ConsolePrint, ReversedPrint
from app.serialize import JsonSerialize, XmlSerialize


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displaying = {
        "console": ConsoleDisplay(),
        "reverse": ReversedDisplay(),
    }

    printing = {
        "console": ConsolePrint(),
        "reverse": ReversedPrint(),
    }

    serialization = {
        "json": JsonSerialize(),
        "xml": XmlSerialize(),
    }
    for cmd, method_type in commands:
        if cmd == "display":
            displaying[method_type].display(book.content)
        elif cmd == "print":
            printing[method_type].print(book.title, book.content)
        elif cmd == "serialize":
            return serialization[method_type].serialize(
                book.title,
                book.content
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
