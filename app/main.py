from app.classes import Book
from app.functions import display, print_book, serialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display(display_type=method_type, book=book)
        elif cmd == "print":
            print_book(print_type=method_type, book=book)
        elif cmd == "serialize":
            return serialize(serialize_type=method_type, book=book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
