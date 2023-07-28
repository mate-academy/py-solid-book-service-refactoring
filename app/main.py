from app.book import Book
from app.utils.display import ConsoleDisplay, ReverseDisplay
from app.utils.print import ConsolePrint, ReversePrint
from app.utils.serialize import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleDisplay.display(book.content)
            elif method_type == "reverse":
                ReverseDisplay.display(book.content)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type == "console":
                ConsolePrint.print(book.title, book.content)
            elif method_type == "reverse":
                ReversePrint.print(book.title, book.content)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type == "json":
                return JsonSerialize.serialize(book.title, book.content)
            elif method_type == "xml":
                return XmlSerialize.serialize(book.title, book.content)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
