from app.book import Book
from app.book_display import DisplayConsole, DisplayReverse
from app.book_print import PrintConsole, PrintReverse
from app.book_serialize import SerializerJSON, SerializerXML


commands_class = {
    ("display", "console"): DisplayConsole,
    ("display", "reverse"): DisplayReverse,
    ("print", "console"): PrintConsole,
    ("print", "reverse"): PrintReverse,
    ("serialize", "json"): SerializerJSON,
    ("serialize", "xml"): SerializerXML
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        method_class = commands_class[(cmd, method_type)]
        method_object = method_class()
        if cmd == "display":
            method_object.display(book=book)
        elif cmd == "print":
            method_object.print(book=book)
        elif cmd == "serialize":
            return method_object.serialize(book=book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
