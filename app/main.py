from app.displayer import ConsoleBookDisplayer, ReverseBookDisplayer
from app.printer import ConsoleBookPrinter, ReverseBookPrinter
from app.serializer import JSONBookSerializer, XMLBookSerializer

DISPLAY_MANAGER = {
    "console": ConsoleBookDisplayer,
    "reverse": ReverseBookDisplayer
}

PRINT_MANAGER = {
    "console": ConsoleBookPrinter,
    "reverse": ReverseBookPrinter
}

SERIALIZE_MANAGER = {
    "json": JSONBookSerializer,
    "xml": XMLBookSerializer
}


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_MANAGER[method_type]().display(book)
        elif cmd == "print":
            PRINT_MANAGER[method_type]().print(book)
        elif cmd == "serialize":
            return SERIALIZE_MANAGER[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
