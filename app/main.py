from app.book import Book
from app.display import BookDisplay
from app.print import BookPrinter
from app.serializers import BookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display = BookDisplay()
    printer = BookPrinter()
    serializer = BookSerializer()

    for cmd, method_type in commands:
        if cmd == "display":
            display.display(book, method_type)
        elif cmd == "print":
            printer.print_book(book, method_type)
        elif cmd == "serialize":
            return serializer.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
