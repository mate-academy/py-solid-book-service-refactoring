from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_ import ConsolePrint, ReversePrint
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    methods = {
        "display": {"console": ConsoleDisplay, "reverse": ReverseDisplay},
        "print": {"console": ConsolePrint, "reverse": ReversePrint},
        "serialize": {"json": JsonSerializer, "xml": XmlSerializer}
    }

    for cmd, method_type in commands:
        if cmd == "display":
            methods[cmd][method_type](book).display()
        elif cmd == "print":
            methods[cmd][method_type](book).print_book()
        elif cmd == "serialize":
            return methods[cmd][method_type](book).serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
