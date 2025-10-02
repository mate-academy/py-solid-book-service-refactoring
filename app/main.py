from app.displays import ConsoleDisplay, ReverseDisplay
from app.models import Book
from app.printers import ConsolePrint, ReversePrint
from app.serializers import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayers = {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    }
    printers = {
        "console": ConsolePrint,
        "reverse": ReversePrint,
    }
    serializers = {
        "json": JsonSerialize,
        "xml": XmlSerialize,
    }

    result = None

    for cmd, method_type in commands:
        if cmd == "display":
            displayer = displayers.get(method_type)
            if displayer is None:
                raise ValueError(f"Unknown display type: {method_type}")
            displayer().display(book)

        elif cmd == "print":
            printer = printers.get(method_type)
            if printer is None:
                raise ValueError(f"Unknown print type: {method_type}")
            printer().print_book(book)

        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            if serializer is None:
                raise ValueError(f"Unknown serialize type: {method_type}")
            result = serializer().serialize(book)

        else:
            raise ValueError(f"Unknown command: {cmd}")

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
