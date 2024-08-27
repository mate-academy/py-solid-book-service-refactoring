from book.book import Book
from book.display import DisplayBook
from book.print import PrintBook
from book.serializers import SerializeBook


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DisplayBook.display(book, method_type)
        elif cmd == "print":
            PrintBook.print(book, method_type)
        elif cmd == "serialize":
            return SerializeBook.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
