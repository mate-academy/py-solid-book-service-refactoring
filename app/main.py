from app.book import Book
from app.printer import BookPrinter
from app.serializer import BookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            BookPrinter.print_book(book, method_type)
        elif cmd == "serialize":
            return BookSerializer.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
