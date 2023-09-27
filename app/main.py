from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display = None
            if method_type == "console":
                display = ConsoleDisplay()
            elif method_type == "reverse":
                display = ReverseDisplay()
            else:
                raise ValueError(f"Unknown display type: {method_type}")
            display.display(book.content)
        elif cmd == "print":
            print_method = None
            if method_type == "console":
                print_method = ConsolePrint()
            elif method_type == "reverse":
                print_method = ReversePrint()
            else:
                raise ValueError(f"Unknown print type: {method_type}")
            print_method.print(book.title, book.content)
        elif cmd == "serialize":
            serializer = None
            if method_type == "json":
                serializer = JsonSerializer()
            elif method_type == "xml":
                serializer = XmlSerializer()
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(
                {"title": book.title, "content": book.content}
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
