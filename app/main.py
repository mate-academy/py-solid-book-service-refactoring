from app.book import (
    Book,
    DisplayBook,
    PrintBook,
    ConsoleDisplay,
    ReverseDisplay,
    ConsolePrint,
    ReversePrint,
)
from app.serializer import SerializeBook, JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    method_types = (
        DisplayBook.display_method
        + PrintBook.print_method
        + SerializeBook.serializer_type
    )

    for cmd, method_type in commands:
        if method_type in method_types:
            if cmd == "display":
                if method_type == "console":
                    ConsoleDisplay.display(book)
                else:
                    ReverseDisplay.display(book)
            elif cmd == "print":
                if method_type == "console":
                    ConsolePrint.print_book(book)
                else:
                    ReversePrint.print_book(book)
            elif cmd == "serialize":
                if method_type == "json":
                    return JSONSerializer.serialize(book)
                else:
                    return XMLSerializer.serialize(book)
        else:
            raise ValueError(f"Unknown method type: {method_type}.")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
