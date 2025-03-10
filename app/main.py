from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_book import ConsolePrint, ReversePrint
from app.serialize import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_methods = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    print_methods = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }

    serialize_methods = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            display_methods[method_type].display(book)
        elif cmd == "print":
            print_methods[method_type].print_book(book)
        elif cmd == "serialize":
            return serialize_methods[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
