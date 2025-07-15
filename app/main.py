from app.book.book import Book
from app.book.display import DisplayConsole, DisplayReverse
from app.book.serialize import SerializeJson, SerializeXml
from app.book.print import PrintConsole, PrintReverse


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                displayer = DisplayConsole()
                displayer.display(book)
            elif method_type == "reverse":
                displayer = DisplayReverse()
                displayer.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type == "console":
                printer = PrintConsole()
                printer.print(book)
            elif method_type == "reverse":
                printer = PrintReverse()
                printer.print(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type == "json":
                serializer = SerializeJson()
                return serializer.serialize(book)
            elif method_type == "xml":
                serializer = SerializeXml()
                return serializer.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
