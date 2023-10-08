from .book import Book
from .display import BookDisplay
from .print import BookPrint
from .serialize import BookSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display = BookDisplay()
            if method_type == "console":
                display.console(book)
            if method_type == "reverse":
                display.reverse(book)
        elif cmd == "print":
            print_b = BookPrint()
            if method_type == "console":
                print_b.console(book)
            if method_type == "reverse":
                print_b.reverse(book)
        elif cmd == "serialize":
            serializer = BookSerialize()
            if method_type == "json":
                return serializer.json(book)
            if method_type == "xml":
                return serializer.xml(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
