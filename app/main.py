from .interface import BookDisplay, BookPrint, BookSerialize
from .model import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    disp = BookDisplay()
    printer = BookPrint()
    serializer = BookSerialize()

    result = None

    for cmd, method_type in commands:
        if cmd == "display":
            disp.display(book, method_type)
        elif cmd == "print":
            printer.print_book(book, method_type)
        elif cmd == "serialize":
            result = serializer.serialize(book, method_type)

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
