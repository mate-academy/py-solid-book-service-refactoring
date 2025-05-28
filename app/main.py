from app.book import Book
from app.display import DisplayRight, DisplayRevers
from app.serializer import SerializerJson, SerializerXML
from app.print import PrintRight, PrintReverse


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display = {
        "console": DisplayRight(),
        "reverse": DisplayRevers(),
    }
    print_b = {
        "console": PrintRight(),
        "reverse": PrintReverse(),
    }
    serializer = {
        "json": SerializerJson(),
        "xml": SerializerXML(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            strategy = display.get(method_type)
            strategy.display(book)
        elif cmd == "print":
            strategy = print_b.get(method_type)
            strategy.print_book(book)
        elif cmd == "serialize":
            strategy = serializer.get(method_type)
            return strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
