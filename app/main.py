from app.display import DisplayConsole, DisplayReverse
from app.printed import PrintConsole, PrintReverse
from app.serializer import JsonSerializer, XmlSerializer
from app.book import Book

all_data = {
    "serialize_type": {"json": JsonSerializer, "xml": XmlSerializer},
    "display_type": {"console": DisplayConsole, "reverse": DisplayReverse},
    "print_type": {"console": PrintConsole, "reverse": PrintReverse},
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            all_data["display_type"].get(method_type)(book).display()
        elif cmd == "print":
            all_data["print_type"].get(method_type)(book).print_book()
        elif cmd == "serialize":
            return (
                all_data["serialize_type"].get(method_type)(book).serialize()
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
