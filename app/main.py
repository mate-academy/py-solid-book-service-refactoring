from typing import Type

from app.book import Book
from app.display_book import DisplayConsole, DisplayReverse, DisplayWay
from app.print_book import PrintConsole, PrintReverse, PrintWay
from app.serialize_book import SerializeJson, SerializeXml, SerializeWay

DISPLAY_STRATEGY: dict[str, Type[DisplayWay]] = {
    "console": DisplayConsole,
    "reverse": DisplayReverse
}
PRINT_STRATEGY: dict[str, Type[PrintWay]] = {
    "console": PrintConsole,
    "reverse": PrintReverse
}

SERIALIZE_STRATEGY: dict[str, Type[SerializeWay]] = {
    "json": SerializeJson,
    "xml": SerializeXml
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_STRATEGY[method_type]().display_book(book)
        elif cmd == "print":
            PRINT_STRATEGY[method_type]().print_book(book)
        elif cmd == "serialize":
            return SERIALIZE_STRATEGY[method_type]().serialize_book(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
