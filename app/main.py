from app.serializers import serialize_factor
from app.displayers import display_factor
from app.printers import print_factor
from app.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    for cmd, method_type in commands:
        if cmd == "display":
            return display_factor(book, method_type)
        elif cmd == "print":
            return print_factor(book, method_type)
        elif cmd == "serialize":
            return serialize_factor(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
