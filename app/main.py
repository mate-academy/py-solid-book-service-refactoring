from app.book import Book
from app.display import Display
from app.book_printer import Printer
from app.book_serializer import Serializer

book_printer = Printer()
book_displayer = Display()
book_serializer = Serializer()


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book_displayer.display_book(method_type, book)
        elif cmd == "print":
            book_printer.go_print(method_type, book)
        elif cmd == "serialize":
            return book_serializer.serialize_book(method_type, book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
