from app.book import Book
from app.display import DisplayBook
from app.printer import PrintBook
from app.serializer import SerializeBook


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_book = DisplayBook(book)
            display_book.display(method_type)
        elif cmd == "print":
            print_book = PrintBook(book)
            print_book.print_book(method_type)
        elif cmd == "serialize":
            serialize_book = SerializeBook(book)
            return serialize_book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
