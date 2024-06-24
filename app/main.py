from app.book import Book
from app.display import ReverseDisplay, ConsoleDisplay
from app.print import ConsolePrint, ReversePrint
from app.serializer import XMLSerializer, JsonSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_mapping = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }

    print_mapping = {
        "console": ConsolePrint(),
        "reverse": ReversePrint()
    }

    serializer_mapping = {
        "json": JsonSerializer(),
        "xml": XMLSerializer()
    }
    for cmd, method_type in commands:
        if cmd == "display":
            display_mapping[method_type].display(book)
        elif cmd == "print":
            print_mapping[method_type].print(book)
        elif cmd == "serialize":
            return serializer_mapping[method_type].serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
