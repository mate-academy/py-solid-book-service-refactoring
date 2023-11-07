from app.book import Book
from app.serializer import BookJSONSerializer, BookXMLSerializer
from app.book import Display, Printer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    serializer_types = {
        "json": BookJSONSerializer(),
        "xml": BookXMLSerializer()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            Display.display(book, method_type)
        elif cmd == "print":
            Printer.print_book(book, method_type)
        elif cmd == "serialize":
            serializer = serializer_types.get(method_type)
            if serializer:
                return serializer.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "json")]))
