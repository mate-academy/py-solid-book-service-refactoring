from app.display import DisplayConsole, DisplayReverse
from app.print import PrintConsole, PrintReverse
from app.serialize import SerializeJSON, SerializeXML


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                display = DisplayConsole()
            elif method_type == "reverse":
                display = DisplayReverse()
            else:
                raise ValueError(f"Unknown display type: {method_type}")
            return display.display_type(book)
        elif cmd == "print":
            if method_type == "console":
                printer = PrintConsole()
                printer.print_type(book)
            elif method_type == "reverse":
                printer = PrintReverse()
                printer.print_type(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type.lower() == "json":
                serializer = SerializeJSON()
            elif method_type.lower() == "xml":
                serializer = SerializeXML()
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
