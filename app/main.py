from app.managers.Book import Book
from app.managers.Display import DisplayConsole, DisplayReverse
from app.managers.Printer import PrintConsole, PrintReverse
from app.managers.Serializer import SerializerJSON, SerializerXML


commands_obj = {
    "display": {
        "console": DisplayConsole(), "reverse": DisplayReverse()
    },
    "print": {
        "console": PrintConsole(), "reverse": PrintReverse()
    },
    "serialize": {
        "json": SerializerJSON(), "xml": SerializerXML()
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            commands_obj[cmd][method_type].display(book)
        elif cmd == "print":
            commands_obj[cmd][method_type].print_book(book)
        elif cmd == "serialize":
            serializer = commands_obj[cmd][method_type]

            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
