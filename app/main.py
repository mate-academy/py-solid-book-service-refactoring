from app.book import Book
from app.managers.display_manager import ConsoleDisplay, ReverseDisplay
from app.managers.print_manager import ConsolePrint, ReversePrint
from app.managers.serialize_manager import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }
    prints = {
        "console": ConsolePrint(),
        "reverse": ReversePrint()
    }
    serializers = {
        "json": JsonSerialize(),
        "xml": XmlSerialize()
    }
    result = None
    for cmd, method_type in commands:
        if cmd == "display":
            displays = displays.get(method_type)
            if displays:
                displays.display(book)

        elif cmd == "print":
            prints = prints.get(method_type)
            if prints:
                prints.print(book)

        elif cmd == "serialize":
            serializers = serializers.get(method_type)
            if serializers:
                result = serializers.serialize(book)

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
