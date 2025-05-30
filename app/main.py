from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serializer import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }
    print_strategies = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }
    serialize_strategies = {
        "json": JsonSerialize(),
        "xml": XmlSerialize(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            book.display(display_strategies[method_type])
        elif cmd == "print":
            book.print_book(print_strategies[method_type])
        elif cmd == "serialize":
            return book.serialize(serialize_strategies[method_type])
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
