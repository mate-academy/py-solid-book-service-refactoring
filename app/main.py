from app.models.models import Book
from app.serializers.json_serializer import JsonSerializer
from app.serializers.xml_serializer import XmlSerializer
from app.strategies.display import ConsoleDisplay, ReverseDisplay
from app.strategies.print import ConsolePrint, ReversePrint


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleDisplay().display(book)
            elif method_type == "reverse":
                ReverseDisplay().display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            if method_type == "console":
                ConsolePrint().print(book)
            elif method_type == "reverse":
                ReversePrint().print(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            if method_type == "json":
                result = JsonSerializer().serialize(book)
            elif method_type == "xml":
                result = XmlSerializer().serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(
        main(
            sample_book,
            [
                ("display", "reverse"),
                ("serialize", "xml")
            ]
        )
    )
