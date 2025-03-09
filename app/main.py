from app.representation import ConsoleRepresentation, ReverseRepresentation
from app.serializers import XMLSerializer, JsonSerializer
from app.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "reverse":
                reverser = ReverseRepresentation()
                reverser.display(book)
            elif method_type == "console":
                console = ConsoleRepresentation()
                console.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type == "reverse":
                reverser = ReverseRepresentation()
                reverser.print_book(book)
            elif method_type == "console":
                console = ConsoleRepresentation()
                console.print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type == "json":
                serializer = JsonSerializer()
                return serializer.serialize(book)
            elif method_type == "xml":
                serializer = XMLSerializer()
                return serializer.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
