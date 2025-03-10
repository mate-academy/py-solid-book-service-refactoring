from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serializers import JSONSerialize, XMLSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    _print = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }

    serializers = {
        "json": JSONSerialize(),
        "xml": XMLSerialize(),
    }

    for cmd, method_type in commands:
        if cmd == "display" and method_type in display:
            display[method_type].display(book)
        elif cmd == "print" and method_type in _print:
            _print[method_type].print_book(book)
        elif cmd == "serialize" and method_type in serializers:
            return serializers[method_type].serialize(book)
        else:
            raise ValueError(f"Unknown command or method type: "
                             f"{cmd}, {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
