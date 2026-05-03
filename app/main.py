from app.books import Book
from app.displays import DisplayBook, DisplayReversedBook
from app.prints import PrintBook, PrintReversedBook
from app.serializers import SerializeBookJSON, SerializeBookXML


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                book = DisplayBook(book)
            elif method_type == "reverse":
                book = DisplayReversedBook(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
            book.display()
        elif cmd == "print":
            if method_type == "console":
                book = PrintBook(book)
            elif method_type == "reverse":
                book = PrintReversedBook(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
            book.print_book()
        elif cmd == "serialize":
            if method_type == "json":
                book = SerializeBookJSON(book)
            elif method_type == "xml":
                book = SerializeBookXML(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return book.serialize()
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
