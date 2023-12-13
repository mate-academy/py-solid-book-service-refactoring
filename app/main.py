from app.book import BookDisplay, BookPrinter, Book
from app.serializers import BookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategy = BookDisplay()
    print_strategy = BookPrinter()

    for cmd, method_type in commands:
        if cmd == "display":
            if hasattr(display_strategy, "display"):
                display_strategy.display(book, method_type)
            else:
                raise AttributeError("Display method not supported.")
        elif cmd == "print":
            if hasattr(print_strategy, "print_book"):
                print_strategy.print_book(book, method_type)
            else:
                raise AttributeError("Print method not supported.")
        elif cmd == "serialize":
            return BookSerializer.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
