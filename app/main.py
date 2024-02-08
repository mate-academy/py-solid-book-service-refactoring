from app.book import Book
from app.displayer import DisplayBookConsole, DisplayBookReverse
from app.printbook import PrintBookConsole, PrintBookReverse
from app.serializer import BookSerializerXML, BookSerializerJSON


interface = {
    "display": {
        "console": DisplayBookConsole,
        "reverse": DisplayBookReverse,
    },
    "print": {
        "console": PrintBookConsole,
        "reverse": PrintBookReverse,
    },
    "serialize": {
        "json": BookSerializerJSON,
        "xml": BookSerializerXML,
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if interface.get(cmd):
            if cmd == "display":
                if method_type in interface[cmd].keys():
                    interface[cmd][method_type]().display(book)
                else:
                    raise ValueError(f"Unknown display type: {method_type}")
            elif cmd == "print":
                if method_type in interface[cmd].keys():
                    interface[cmd][method_type]().print(book)
                else:
                    raise ValueError(f"Unknown print type: {method_type}")
            elif cmd == "serialize":
                if method_type in interface[cmd].keys():
                    return interface[cmd][method_type]().serialize(book)
                else:
                    raise ValueError(f"Unknown serialize type: {method_type}")
        else:
            raise ValueError(f"Invalid command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
