from app.book import Book
from app.display import Display
from app.print_book import PrintBook
from app.serialize import Serialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            Display.display(book, method_type)
        elif cmd == "print":
            PrintBook.print_book(book, method_type)
        elif cmd == "serialize":
            return Serialize.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
