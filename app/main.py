from app.book import Book
from app.display.console import ConsoleDisplay
from app.display.reverse import ReverseDisplay
from app.printing.console import ConsolePrinter
from app.printing.reverse import ReversePrinter
from app.serialization.json_serializer import SerializeBookJson
from app.serialization.xml_serializer import SerializeBookXml

display_types = {"console": ConsoleDisplay, "reverse": ReverseDisplay}
print_types = {"console": ConsolePrinter, "reverse": ReversePrinter}
serialize_types = {"json": SerializeBookJson, "xml": SerializeBookXml}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_book = display_types[method_type]()
            display_book.display_content(book)
        elif cmd == "print":
            printing_book = print_types[method_type]()
            printing_book.print_book(book)
        elif cmd == "serialize":
            serialize_book = serialize_types[method_type]()
            return serialize_book.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
