from app.book import Book
from app.displayers import ConsoleDisplay, ReverseDisplay
from app.printers import ConsolePrint, ReversePrint
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }

    print_strategies = {
        "console": ConsolePrint(),
        "reverse": ReversePrint()
    }

    serialize_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    }

    for cmd, method_type in commands:
        if cmd == "display" and method_type in display_strategies:
            display_strategies[method_type].display(book.content)
        elif cmd == "print" and method_type in print_strategies:
            print_strategies[method_type].print_book(book.title, book.content)
        elif cmd == "serialize" and method_type in serialize_strategies:
            return (
                serialize_strategies[method_type]
                .serialize(book.title, book.content)
            )
        else:
            raise ValueError(
                f"Unknown command or method type: {cmd}, {method_type}"
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    result = main(sample_book, [
        ("display", "reverse"),
        ("serialize", "xml")
    ])
    if result:
        print(result)
