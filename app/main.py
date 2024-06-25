from .book import Book
from .display import BookDisplayer
from .print import BookPrinter
from .serializers import BookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            BookDisplayer.display(book=book, display_type=method_type)
        elif cmd == "print":
            BookPrinter.print_book(book=book, print_type=method_type)
        elif cmd == "serialize":
            return BookSerializer.serialize(
                book=book, serialize_type=method_type
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
