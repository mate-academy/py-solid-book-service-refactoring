from app.book import Book
from app.display import ReverseDisplay, ConsoleDisplay
from app.print import ReversePrinter, ConsolePrinter
from app.serializers import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "reverse":
                displayer = ReverseDisplay(book)
            else:
                displayer = ConsoleDisplay(book)
            displayer.display()
        elif cmd == "print":
            if method_type == "reverse":
                printer = ReversePrinter(book)
            else:
                printer = ConsolePrinter(book)
            printer.print()
        elif cmd == "serialize":
            if method_type == "json":
                serializer = JSONSerializer(book)
            else:
                serializer = XMLSerializer(book)
            return serializer.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
