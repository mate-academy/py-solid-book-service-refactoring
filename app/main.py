from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print import PrintConsole, PrintReverse
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    methods = {
        "display": {"console": DisplayConsole, "reverse": DisplayReverse},
        "print": {"console": PrintConsole, "reverse": PrintReverse},
        "serialize": {"json": JsonSerializer, "xml": XmlSerializer},
    }

    for cmd, method_type in commands:
        try:
            if cmd == "display":
                methods[cmd][method_type](book).display()
            elif cmd == "print":
                methods[cmd][method_type](book).print()
            elif cmd == "serialize":
                return methods[cmd][method_type](book).serialize()
            else:
                raise ValueError("Unknown method")
        except ValueError:
            print(f"Unknown {cmd} type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
