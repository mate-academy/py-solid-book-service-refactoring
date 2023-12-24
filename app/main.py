from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printing import ConsolePrint, ReversePrint
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                displayer = ConsoleDisplay(book)
            elif method_type == "reverse":
                displayer = ReverseDisplay(book)
            else:
                raise ValueError(f"Unknown display type {method_type}")
            displayer.display_book()

        elif cmd == "print":
            if method_type == "console":
                prints = ConsolePrint(book)
            elif method_type == "reverse":
                prints = ReversePrint(book)
            else:
                raise ValueError(f"Unknown print type {method_type}")
            prints.print_book()

        elif cmd == "serialize":
            serializers = {
                "json": JsonSerializer,
                "xml": XmlSerializer,
            }
            serializer_class = serializers.get(method_type)
            if serializer_class:
                serializer = serializer_class(book)
                return serializer.serialize_book()
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
