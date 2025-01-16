from app.models import Book
from app.view import BookView, BookPrinter
from app.serializer import JSONBookSerializer, XMLBookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            BookView.display(book, method_type)
        elif cmd == "print":
            BookPrinter.print_book(book, method_type)
        elif cmd == "serialize":
            if method_type == "json":
                return JSONBookSerializer.serialize(book)
            elif method_type == "xml":
                return XMLBookSerializer.serialize(book)
            else:
                raise ValueError(f"Unknown serialization type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
