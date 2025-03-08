from app.book import Book
from app.serializers import JsonSerializer, XMLSerializer
from app.representation import ConsoleRepresentation, ReverseRepresentation


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    ways_of_representation = {
        "console": ConsoleRepresentation(),
        "reverse": ReverseRepresentation(),
    }
    serializers_to_choose = {
        "json": JsonSerializer(),
        "xml": XMLSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type in ways_of_representation:
                ways_of_representation[method_type].display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type in ways_of_representation:
                ways_of_representation[method_type].print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type in serializers_to_choose:
                return serializers_to_choose[method_type].serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
