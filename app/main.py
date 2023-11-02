from app.book import Book
from app.display import ReverseDisplay, ConsoleDisplay
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {
        "reverse": ReverseDisplay,
        "console": ConsoleDisplay,
    }

    methods = {
        "display": displays,
        "print": displays,
        "serialize": {
            "json": JsonSerializer,
            "xml": XmlSerializer,
        }
    }

    for cmd, method_type in commands:
        if cmd == "display":
            methods[cmd][method_type]().display(book)
        elif cmd == "print":
            methods[cmd][method_type]().print_book(book)
        elif cmd == "serialize":
            return methods[cmd][method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
