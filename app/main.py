from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_book import ConsolePrint, ReversePrint
from app.serializers import JsonSerialize, XmlSerialize

DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINT_STRATEGIES = {
    "console": ConsolePrint,
    "reverse": ReversePrint,
}

SERIALIZE_STRATEGIES = {
    "json": JsonSerialize,
    "xml": XmlSerialize,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_STRATEGIES[method_type]().display(book)
        elif cmd == "print":
            PRINT_STRATEGIES[method_type]().print_book(book)
        elif cmd == "serialize":
            return SERIALIZE_STRATEGIES[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
