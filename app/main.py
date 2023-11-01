from app.book import Book
from app.display import ConsoleDisplayBook, ReverseDisplayBook
from app.printer import ConsolePrintBook, ReversePrintBook
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displaying = {
        "console": ConsoleDisplayBook(),
        "reverse": ReverseDisplayBook(),
    }

    printing = {
        "console": ConsolePrintBook(),
        "reverse": ReversePrintBook(),
    }

    serialization = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            displaying[method_type].display(book)
        elif cmd == "print":
            printing[method_type].print_book(book)
        elif cmd == "serialize":
            return serialization[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
