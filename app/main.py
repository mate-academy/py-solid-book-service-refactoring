from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serialization import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_type = {
                "console": ConsoleDisplay(),
                "reverse": ReverseDisplay()
            }.get(method_type)

            display_type.display_content(book)
        elif cmd == "print":
            printer = {
                "console": ConsolePrinter(),
                "reverse": ReversePrinter()
            }.get(method_type)

            printer.print_content(book)
        elif cmd == "serialize":
            serializer = {
                "json": JsonSerializer(),
                "xml": XmlSerializer(),
            }.get(method_type)

            if not serializer:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
