from app.book import Book
from app.print_manager import PrintBookConsole, PrintBookReverse
from app.display_manager import DisplayBookConsole, DisplayBookReverse
from app.serialize_manager import SerializeXML, SerializeJson


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "print":
            if method_type == "console":
                PrintBookConsole(book=book).print_book()
            elif method_type == "reverse":
                PrintBookReverse(book=book).print_book()
            else:
                print(f"Unknown print type: {method_type}")
        if cmd == "display":
            if method_type == "console":
                DisplayBookConsole(book=book).display()
            elif method_type == "reverse":
                DisplayBookReverse(book=book).display()
            else:
                print(f"Unknown display type: {method_type}")
        elif cmd == "serialize":
            if method_type == "json":
                return SerializeJson(book=book).serialize_book()
            elif method_type == "xml":
                return SerializeXML(book=book).serialize_book()
            else:
                print(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
