from app.factory import (
    DisplayFactory,
    PrintFactory,
    SerializeFactory
)
from app.models import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            proc = DisplayFactory.get(method_type)
            proc.display(book)
        elif cmd == "print":
            proc = PrintFactory.get(method_type)
            proc.print(book)
        elif cmd == "serialize":
            proc = SerializeFactory.get(method_type)
            return proc.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
