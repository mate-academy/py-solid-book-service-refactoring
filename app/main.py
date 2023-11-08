from __future__ import annotations

from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serialize import XmlSerialize, JsonSerialize


displays = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}
printers = {
    "console": ConsolePrint,
    "reverse": ReversePrint,
}
serialization = {
    "json": JsonSerialize,
    "xml": XmlSerialize,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            displays[method_type].display(method_type, book)
        elif cmd == "print":
            printers[method_type].print_book(book, book.title, book.content)
        elif cmd == "serialize":
            return serialization[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
