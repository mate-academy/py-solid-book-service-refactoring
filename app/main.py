from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printing import ConsolePrint, ReversePrint
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if cmd == "console":
                displayer = ConsoleDisplay(book)
            elif cmd == "reverse":
                displayer = ReverseDisplay(book)
            else:
                raise ValueError("Unknown display type ...")
            displayer.display_book()

        elif cmd == "print":
            if method_type == "console":
                prints = ConsolePrint(book)
            elif method_type == "reverse":
                prints = ReversePrint(book)
            else:
                raise ValueError("Unknown print type ...")
            prints.print_book()

        elif cmd == "serialize":
            if method_type == "json":
                serializer = JsonSerializer(book)
            elif method_type == "xml":
                serializer = XmlSerializer(book)
            else:
                raise ValueError("Unknown serialize type")
            return serializer.serialize_book()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
