from app.book import Book
from app.book_display import ReverseDisplay, ConsoleDisplay
from app.book_print import ReversePrintBook, ConsolePrintBook
from app.book_serializer import JSONBookSerializer, XMLBookSerializer


data = {
    "serialize": {"json": JSONBookSerializer, "xml": XMLBookSerializer},
    "display": {"console": ConsoleDisplay, "reverse": ReverseDisplay},
    "print_book": {"console": ConsolePrintBook, "reverse": ReversePrintBook},
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            data.get("display").get(method_type)(book).display()
        elif cmd == "print":
            data.get("print_book").get(method_type)(book).print_book()
        elif cmd == "serialize":
            return data.get("serialize").get(method_type)(book).serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
