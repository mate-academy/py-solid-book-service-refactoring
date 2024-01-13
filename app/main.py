from app.books import Book
from app.display import ConsoleDisplayService, ReverseDisplayService
from app.print import ConsolePrintService, ReversePrintService
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                display_book = ConsoleDisplayService(book)
            elif method_type == "reverse":
                display_book = ReverseDisplayService(book)
            else:
                raise ValueError("Unknown display type")
            display_book.display()

        elif cmd == "print":
            if method_type == "console":
                print_book = ConsolePrintService(book)
            elif method_type == "reverse":
                print_book = ReversePrintService(book)
            else:
                raise ValueError("Unknown print type")
            print_book.print()

        elif cmd == "serialize":
            if method_type == "json":
                serializer_book = JsonSerializer(book)
            elif method_type == "xml":
                serializer_book = XmlSerializer(book)
            else:
                raise ValueError("Unknown serializer type")
            return serializer_book.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
