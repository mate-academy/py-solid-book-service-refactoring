from app.books import BookReverse, BookConsole, Book
from app.serializers import SerializerToJson, SerializerToXml

CMD = {
    "display": "display",
    "print": "print_book",
    "serialize": "serialize"
}

METHOD = {
    "reverse": BookReverse,
    "console": BookConsole,
    "json": SerializerToJson,
    "xml": SerializerToXml,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        obj = METHOD[method_type]()
        cmd = CMD[cmd]
        return getattr(obj, cmd)(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
