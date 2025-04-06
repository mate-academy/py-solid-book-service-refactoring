from app.models import Book
from app.processors import display_processors, print_processors, serializers


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    result = None
    for cmd, method_type in commands:
        if cmd == "display" and method_type in display_processors:
            display_processors[method_type].display(book)
        elif cmd == "print" and method_type in print_processors:
            print_processors[method_type].print(book)
        elif cmd == "serialize" and method_type in serializers:
            result = serializers[method_type].serialize(book)

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
