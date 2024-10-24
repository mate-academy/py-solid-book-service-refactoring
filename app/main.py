from typing import Type

from app.book import Book
from app.serializer import JsonSerializer, XmlSerializer, SerializerStrategy
from app.printer import ConsolePrint, ReversePrint, PrintStrategy
from app.display import ConsoleDisplay, ReverseDisplay, DisplayStrategy

DISPLAY_STRATEGIES: dict[str, Type[DisplayStrategy]] = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINT_STRATEGIES: dict[str, Type[PrintStrategy]] = {
    "console": ConsolePrint,
    "reverse": ReversePrint,
}

SERIALIZER_STRATEGIES: dict[str, Type[SerializerStrategy]] = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_STRATEGIES[method_type]().display(book.content)

        elif cmd == "print":
            PRINT_STRATEGIES[method_type]().print_book(
                book.title,
                book.content
            )

        elif cmd == "serialize":
            return SERIALIZER_STRATEGIES[method_type]().serialize(
                book.title,
                book.content
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
