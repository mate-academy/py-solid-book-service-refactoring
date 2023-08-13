from app.book import Book
from app.book_displayers import BookConsoleDisplayer, BookReverseDisplayer
from app.book_printers import BookConsolePrinter, BookReversePrinter
from app.book_serializers import BookJSONSerializer, BookXMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                book = BookConsoleDisplayer(book.title, book.content)
            elif method_type == "reverse":
                book = BookReverseDisplayer(book.title, book.content)
            book.display()
        elif cmd == "print":
            if method_type == "console":
                book = BookConsolePrinter(book.title, book.content)
            elif method_type == "reverse":
                book = BookReversePrinter(book.title, book.content)
            book.print_book()
        elif cmd == "serialize":
            if method_type == "json":
                book = BookJSONSerializer(book.title, book.content)
            elif method_type == "xml":
                book = BookXMLSerializer(book.title, book.content)
            return book.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
