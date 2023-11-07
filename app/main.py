from app.book import Book
from app.book_display import ConsoleDisplay, ReverseDisplay
from app.print_book import ConsoleBookPrinter, ReverseBookPrinter
from app.book_serializer import JsonSerializer, XmlSerializer


handlers = {
    "display": {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    },
    "print": {
        "console": ConsoleBookPrinter(),
        "reverse": ReverseBookPrinter()
    },
    "serialize": {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None
    for cmd, method_type in commands:
        if cmd == "display":
            handlers[cmd][method_type].display(book)
        elif cmd == "print":
            handlers[cmd][method_type].print_book(book)
        elif cmd == "serialize":
            result = handlers[cmd][method_type].serialize(book)
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
