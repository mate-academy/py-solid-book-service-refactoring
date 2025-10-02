from app.displays import (
    ConsoleDisplay,
    ReverseDisplay,
    ConsolePrinter,
    ReversePrinter
)
from app.models import Book
from app.serializers import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    serializers = {
        "json": JSONSerializer(),
        "xml": XMLSerializer(),
    }

    methods = {
        "display_console": ConsoleDisplay(),
        "display_reverse": ReverseDisplay(),
        "print_console": ConsolePrinter(),
        "print_reverse": ReversePrinter(),
    }

    for cmd, method_type in commands:
        if cmd in ("display", "print"):
            method = methods.get(f"{cmd}_{method_type}")
            if method:
                method.display(book)
        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            if serializer:
                return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
