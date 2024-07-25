from app.book import Book
from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JSONSerialize, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    methods = {
        "display": {"console": ConsoleDisplayer, "reverse": ReverseDisplayer},
        "print": {"console": ConsolePrinter, "reverse": ReversePrinter},
        "serialize": {"json": JSONSerialize, "xml": XMLSerializer}
    }

    for cmd, method_type in commands:
        if cmd == "display":
            methods[cmd][method_type]().display(book)
        elif cmd == "print":
            methods[cmd][method_type]().print(book)
        elif cmd == "serialize":
            return methods[cmd][method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
