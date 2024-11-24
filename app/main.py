from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serialization import JSONSerialization, XMLSerialization


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_methods = {
        "console": ConsoleDisplay(), "reverse": ReverseDisplay(),
    }
    print_methods = {
        "console": ConsolePrint(), "reverse": ReversePrint(),
    }
    serialization_methods = {
        "json": JSONSerialization(), "xml": XMLSerialization(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            display_method = display_methods.get(method_type)
            if display_method:
                book.display(display_method)
            else:
                print(f"Unknown display type: {method_type}")
        elif cmd == "print":
            print_method = print_methods.get(method_type)
            if print_method:
                book.print_book(print_method)
            else:
                print(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            serialization_method = serialization_methods.get(method_type)
            if serialization_method:
                return book.serialize(serialization_method)
            else:
                print(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
