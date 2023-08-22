from app.book import Book
from app.display import DisplayProceed
from app.printer import PrinterProceed
from app.serializer import SerializerProceed


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    book_printer = PrinterProceed()
    book_displayer = DisplayProceed()
    book_serializer = SerializerProceed()
    for cmd, method_type in commands:
        if cmd == "display":
            book_displayer.display_book(method_type, book)
        elif cmd == "print":
            book_printer.go_print(method_type, book)
        elif cmd == "serialize":
            return book_serializer.serialize_book(method_type, book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "console"), ("serialize", "xml")]))
