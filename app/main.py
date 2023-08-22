from app.book import Book
from app.display_book import Display
from app.print_book import Print
from app.serializers import Serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            Display.display_by_type(display_type=method_type, book=book)
        elif cmd == "print":
            Print.print_by_type(print_type=method_type, book=book)
        elif cmd == "serialize":
            return Serializer.serializer_by_type(serialize_type=method_type,
                                                 book=book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
