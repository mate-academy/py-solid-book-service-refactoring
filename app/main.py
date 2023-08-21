from app.book.book import Book
from app.book.book_priner import print_book
from app.book.display import display_book
from app.book.serializers import serialize_book


def main(book: "Book", commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:

        if cmd == "display":
            display_book(book, method_type)

        elif cmd == "print":
            print_book(book, method_type)

        elif cmd == "serialize":
            return serialize_book(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
