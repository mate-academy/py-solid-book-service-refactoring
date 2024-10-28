from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrint, ReversePrint
from app.serializer import SerializerJSON, SerializerXML


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "reverse":
                method = ReverseDisplay()
            else:
                method = ConsoleDisplay()
            book.display(method)
        elif cmd == "print":
            if method_type == "reverse":
                method = ReversePrint()
            else:
                method = ConsolePrint()
            book.print(method)
        elif cmd == "serialize":
            if method_type == "xml":
                method = SerializerXML()
            else:
                method = SerializerJSON()
            return book.serialize(method)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
