from app.book_implementation import Book
from app.print_manage import ConsolePrint, ReversePrint
from app.serializer_manage import XmlBookSerialize, JsonBookSerialize
from app.display_manage import ConsoleDisplay, ReverseDisplay


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "reverse":
                ReverseDisplay.display(book)
            elif method_type == "console":
                ConsoleDisplay.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        if cmd == "print":
            if method_type == "reverse":
                ReversePrint.print_book(book)
            elif method_type == "console":
                ConsolePrint.print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            if method_type == "json":
                return JsonBookSerialize.serialize_book(book)
            elif method_type == "xml":
                return XmlBookSerialize.serialize_book(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
