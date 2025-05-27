from app.book import Book
from app.display_strategies import Display, DisplayConsole, DisplayReverse
from app.print_strategies import ConsolePrinter, ReversePrinter
from app.serialize_strategies import JsonSerializer, XmlSerializer


def run_command(book: Book, command: str, method_type: str) -> str | None:
    if command == "display":
        if method_type == "console":
            Display(DisplayConsole()).display(book.content)
        elif method_type == "reverse":
            Display(DisplayReverse()).display(book.content)
        else:
            raise ValueError(f"Unknown display type: {method_type}")

    elif command == "print":
        if method_type == "console":
            ConsolePrinter().print(book)
        elif method_type == "reverse":
            ReversePrinter().print(book)
        else:
            raise ValueError(f"Unknown print type: {method_type}")

    elif command == "serialize":
        if method_type == "json":
            return JsonSerializer().serialize(book)
        elif method_type == "xml":
            return XmlSerializer().serialize(book)
        else:
            raise ValueError(f"Unknown serialize type: {method_type}")

    else:
        raise ValueError(f"Unknown command: {command}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None
    for command, method_type in commands:
        result = run_command(book, command, method_type)
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
