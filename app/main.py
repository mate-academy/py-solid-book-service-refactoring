from typing import Type

from app.book import Book
from app.display import Display, ConsoleDisplay, ReverseDisplay
from app.serialize import Serialize, JSONSerialize, XMLSerialize
from app.print import Print, ConsolePrint, ReversePrint


display_strategy: dict[str, Type[Display]] = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

print_strategy: dict[str, Type[Print]] = {
    "console": ConsolePrint,
    "reverse": ReversePrint,
}

serializer_strategy: dict[str, Type[Serialize]] = {
    "json": JSONSerialize,
    "xml": XMLSerialize,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_strategy[method_type]().display(book.content)

        elif cmd == "print":
            print_strategy[method_type]().print_book(book)

        elif cmd == "serialize":
            return serializer_strategy[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
