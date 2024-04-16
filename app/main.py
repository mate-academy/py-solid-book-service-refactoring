from app.book import Book
from app import printer, display, serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book_display = display.create_display_behavior(method_type)
            book_display.print_display(book)
        elif cmd == "print":
            book_printer = printer.create_printer_behavior(method_type)
            book_printer.print_book(book)
        elif cmd == "serialize":
            book_serializer = serializer.serialize_book(method_type)
            return book_serializer.serialize_book(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
