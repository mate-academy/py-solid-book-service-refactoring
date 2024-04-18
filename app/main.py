from book.book import Book
from book.display import BookDisplayer
from book.print_book import BookPrinter
from book.serializers import BookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            BookDisplayer.display(book, method_type)
        elif cmd == "print":
            BookPrinter.print_book(book, method_type)
        elif cmd == "serialize":
            return BookSerializer.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
