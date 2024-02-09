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
        interface_type = interface.get(cmd)

        if interface_type is None:
            print(f"Invalid command: {interface_type}")

        handler = interface_type.get(method_type)
        if method_type:
            if cmd == "serialize":
                return handler().serialize(book)
            elif cmd == "print":
                handler().print(book)
            else:
                handler().display(book)
        else:
            print(f"Invalid method type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
