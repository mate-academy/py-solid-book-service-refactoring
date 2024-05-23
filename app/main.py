from app.book import Book
from app.display_book import DisplayConsole, DisplayReverse
from app.serializer import JSONSerializer, XMLSerializer
from app.print_book import PrintConsole, PrintReverse


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    methods = {
        "display": {"console": DisplayConsole, "reverse": DisplayReverse},
        "print": {"console": PrintConsole, "reverse": PrintReverse},
        "serialize": {"json": JSONSerializer, "xml": XMLSerializer},
    }
    for cmd, method_type in commands:
        try:
            if cmd == "display":
                methods[cmd][method_type](book).display()
            elif cmd == "print":
                methods[cmd][method_type](book).print_book()
            elif cmd == "serialize":
                return methods[cmd][method_type](book).serialize()
        except ValueError as error:
            print("You got an invalid command!", error)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
