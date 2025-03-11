from app.models import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printing import ConsolePrint, ReversePrint
from app.serialization import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None:
    display_processors = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }
    print_processors = {
        "console": ConsolePrint(),
        "reverse": ReversePrint()
    }
    serializers = {
        "json": JSONSerializer(),
        "xml": XMLSerializer()
    }
    result = None
    for cmd, method_type in commands:
        if cmd == "display" and method_type in display_processors:
            display_processors[method_type].display(book)
        elif cmd == "print" and method_type in print_processors:
            print_processors[method_type].print(book)
        elif cmd == "serialize" and method_type in serializers:
            result = serializers[method_type].serialize(book)

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
