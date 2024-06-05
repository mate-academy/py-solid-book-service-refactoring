from typing import Type

from app.books import Book
from app.display import DisplayConsole, DisplayReverse, Display
from app.print import PrintConsole, PrintReverse, Print
from app.serializers import Serializer, SerializerJSON, SerializerXML

DISPLAY_STRATEGIES: dict[str, Type[Display]] = {
    "console": DisplayConsole,
    "reverse": DisplayReverse,
}

PRINT_STRATEGIES: dict[str, Type[Print]] = {
    "console": PrintConsole,
    "reverse": PrintReverse,
}

SERIALIZER_STRATEGIES: dict[str, Type[Serializer]] = {
    "json": SerializerJSON,
    "xml": SerializerXML,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_STRATEGIES[method_type]().display(book.content)
        elif cmd == "print":
            PRINT_STRATEGIES[method_type]().print_book(book)
        elif cmd == "serialize":
            return SERIALIZER_STRATEGIES[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
