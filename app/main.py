from app.book import Book
from app.display_book import DisplayConsole, DisplayReverse
from app.print_book import PrintBookConsole, PrintBookReverse
from app.serializer_book import SerializeXml, SerializeJson


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                DisplayConsole.display(book)
            elif method_type == "reverse":
                DisplayReverse.display(book)
        elif cmd == "print":
            if method_type == "console":
                PrintBookConsole.print_book(book)
            elif method_type == "reverse":
                PrintBookReverse.print_book(book)
        elif cmd == "serialize":
            if method_type == "xml":
                xlm = SerializeXml.serialize_book(book)
                return xlm
            elif method_type == "json":
                json_serializer = SerializeJson.serialize_book(book)
                return json_serializer


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
