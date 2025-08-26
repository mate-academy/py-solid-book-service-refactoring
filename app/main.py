from app.book import Book
from app.display_module import ConsoleDisplayer, ReverseDisplayer
from app.print_module import ConsolePrinter, ReversePrinter
from app.serialization_module import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayers = {
        "console": ConsoleDisplayer(),
        "reverse": ReverseDisplayer(),
    }
    printers = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }
    serializers = {
        "json": JSONSerializer(),
        "xml": XMLSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type in displayers:
                displayers[method_type].display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type in printers:
                printers[method_type].print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type in serializers:
                return serializers[method_type].serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")

    print("--- Testing 'display' and 'serialize' ---")
    result = main(sample_book, [("display", "reverse"), ("serialize", "xml")])
    print(f"Serialization result: {result}")

    print("\n--- Testing 'print' ---")
    main(sample_book, [("print", "console")])