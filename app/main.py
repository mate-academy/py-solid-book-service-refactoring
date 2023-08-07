from app.book import Book
from app.display import ReverseDisplay, ConsoleDisplay
from app.print import ReversePrint, ConsolePrint
from app.serializer import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleDisplay.display(book)
            elif method_type == "reverse":
                ReverseDisplay.display(book)
            else:
                raise ValueError(f"Unknown method type: {method_type}.")

        elif cmd == "print":
            if method_type == "console":
                ConsolePrint.print_book(book)
            elif method_type == "reverse":
                ReversePrint.print_book(book)
            else:
                raise ValueError(f"Unknown method type: {method_type}.")

        elif cmd == "serialize":
            if method_type == "json":
                return JSONSerializer.serialize(book)
            elif method_type == "xml":
                return XMLSerializer.serialize(book)
            else:
                raise ValueError(f"Unknown method type: {method_type}.")
        else:
            raise ValueError(f"Unknown method: {cmd}.")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
