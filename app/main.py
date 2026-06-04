from app.book import Book
from app.display import Display
from app.print import Print
from app.serializers import Serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            Display(book, method_type).dispatch()
        elif cmd == "print":
            Print(book, method_type).dispatch()
        elif cmd == "serialize":
            return Serializer(book, method_type).dispatch()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
