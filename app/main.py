from app.factories import display_factory, printer_factory, serializer_factory
from app.models import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None
    for cmd, method_type in commands:
        if cmd == "display":
            displayer = display_factory(method_type)
            displayer.display(book)
        elif cmd == "print":
            printer = printer_factory(method_type)
            printer.print_book(book)
        elif cmd == "serialize":
            serializer = serializer_factory(method_type)
            result = serializer.serialize(book)
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
