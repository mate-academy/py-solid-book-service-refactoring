from app.book import Book
from app.book_printer import ConsolePrint, ReversePrint
from app.display import ConsoleDisplay, ReverseDisplay
from app.serializers import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    printers = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }

    serialization = {
        "json": JsonSerialize(),
        "xml": XmlSerialize(),
    }
    for cmd, method_type in commands:
        if cmd == "display":
            displays[method_type].display(book.content)
        elif cmd == "print":
            printers[method_type].print(book.title, book.content)
        elif cmd == "serialize":
            return serialization[method_type].serialize(
                book.title,
                book.content
            )
