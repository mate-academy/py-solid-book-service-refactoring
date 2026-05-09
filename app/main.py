from app.book import Book
from app.book_display import BookDisplay
from app.book_print import BookPrint
from app.book_serialize import BookSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            BookDisplay.display(book, method_type)
        elif cmd == "print":
            BookPrint.print_book(book, method_type)
        elif cmd == "serialize":
            return BookSerialize.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
