from app.book import Book
from app.display_book import ConsoleDisplayBook, ReverseDisplayBook
from app.print_book import ConsolePrintBook, ReversePrintBook
from app.serializer_book import JsonSerializer, XmlSerializer

data = {
    "display": {
        "console": ConsoleDisplayBook, "reverse": ReverseDisplayBook,
    },
    "print": {
        "console": ConsolePrintBook, "reverse": ReversePrintBook,
    },
    "serialize": {
        "json": JsonSerializer, "xml": XmlSerializer,
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            data.get("display").get(method_type)(book).display()
        elif cmd == "print":
            data.get("print").get(method_type)(book).print_book()
        elif cmd == "serialize":
            return data.get("serialize").get(method_type)(book).serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
