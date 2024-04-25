from app.book import Book
from app import printer, displayer, serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book_displayer = displayer.create_book_displayer(method_type)
            book_displayer.print_display(book)
        elif cmd == "print":
            book_printer = printer.create_book_printer(method_type)
            book_printer.print_book(book)
        elif cmd == "serialize":
            book_serializer = serializer.create_book_serializer(method_type)
            return book_serializer.serialize_book(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
