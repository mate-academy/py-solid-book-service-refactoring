from app.book import Book
from app.display import Display
from app.print_book import PrintBook
from app.serialization import Serialization


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            Display.display(book, method_type)
        elif cmd == "print":
            PrintBook.print_type(book, method_type)
        elif cmd == "serialize":
            return Serialization.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
