from app.get_commands import get_display, get_printer, get_serializer
from app.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display = get_display(method_type)
            display.display(book)
        elif cmd == "print":
            printer = get_printer(method_type)
            printer.print_book(book)
        elif cmd == "serialize":
            serializer = get_serializer(method_type)
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
