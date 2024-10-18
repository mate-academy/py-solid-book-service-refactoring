from app.models import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import Printer
from app.serializers import Serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "reverse":
                ReverseDisplay().display(book)
            else:
                ConsoleDisplay().display(book)
        elif cmd == "print":
            Printer.print_book(book, method_type)
        elif cmd == "serialize":
            return Serializer.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "json")]))
