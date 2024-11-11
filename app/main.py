from app.book import Book
from app.displays import ConsoleDisplay, ReverseDisplay
from app.prints import ConsolePrint, ReversePrint
from app.serializers import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                display_ = ConsoleDisplay()
            elif method_type == "reverse":
                display_ = ReverseDisplay()
            display_.display(book)
        elif cmd == "print":
            if method_type == "console":
                print_ = ConsolePrint()
            elif method_type == "reverse":
                print_ = ReversePrint()
            print_.print_book(book)
        elif cmd == "serialize":
            if method_type == "xml":
                serializer = XMLSerializer()
            elif method_type == "json":
                serializer = JSONSerializer()
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
