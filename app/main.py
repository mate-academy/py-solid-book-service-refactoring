from app.book import Book
from app.display_book import ConsoleDisplayBook, ReverseDisplayBook
from app.print_book import ConsolePrintBook, ReversePrintBook
from app.serialize_book import JsonSerializerBook, XmlSerializerBook


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    # Map commands and method types to classes
    display_methods = {
        "console": ConsoleDisplayBook(),
        "reverse": ReverseDisplayBook(),
    }
    print_methods = {
        "console": ConsolePrintBook(),
        "reverse": ReversePrintBook(),
    }
    serialize_methods = {
        "json": JsonSerializerBook(),
        "xml": XmlSerializerBook(),
    }

    for cmd, method_type in commands:
        if cmd == "display" and method_type in display_methods:
            display_methods[method_type].display(book)
        elif cmd == "print" and method_type in print_methods:
            print_methods[method_type].print(book)
        elif cmd == "serialize" and method_type in serialize_methods:
            return serialize_methods[method_type].serialize(book)
        else:
            raise ValueError(
                f"Invalid command or method type: {cmd}, {method_type}"
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
