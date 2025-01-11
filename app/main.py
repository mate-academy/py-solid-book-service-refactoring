from app.book import Book
from app.displays import choose_display_type
from app.printers import choose_printer
from app.serializers import choose_serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book_display = choose_display_type(method_type)
            book_display.display(book)
        elif cmd == "print":
            book_printer = choose_printer(method_type)
            book_printer.print_book(book)
        elif cmd == "serialize":
            book_serializer = choose_serializer(method_type)
            return book_serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
