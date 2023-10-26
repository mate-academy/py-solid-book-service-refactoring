from app.book import Book
from app.print_book import PrintBook
from app.book_display import BookDisplay
from app.book_serialize import BookSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_book = BookDisplay(book)
            if hasattr(display_book, method_type):
                getattr(display_book, method_type)()
            else:
                raise ValueError("Unknown display type.")
        elif cmd == "print":
            print_book = PrintBook(book)
            if hasattr(print_book, method_type):
                getattr(print_book, method_type)()
            else:
                raise ValueError("Unknown print type.")
        elif cmd == "serialize":
            serialize_book = BookSerialize(book)
            if hasattr(serialize_book, "to_" + method_type):
                print(getattr(serialize_book, "to_" + method_type)())
                return getattr(serialize_book, "to_" + method_type)()
            else:
                raise ValueError("Unknown serialize type.")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
