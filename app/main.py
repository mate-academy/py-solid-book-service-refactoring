from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_type import ConsolePrint, ReversePrint
from app.serializers import JSONSerializer, XMLSerializer


DISPLAY_TYPES = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}
PRINT_TYPES = {
    "console": ConsolePrint,
    "reverse": ReversePrint,
}
SERIALIZE_TYPE = {
    "json": JSONSerializer,
    "xml": XMLSerializer,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_TYPES[method_type]().display(book)
        elif cmd == "print":
            PRINT_TYPES[method_type]().print_book(book)
        elif cmd == "serialize":
            return SERIALIZE_TYPE[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
