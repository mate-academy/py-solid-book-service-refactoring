from app.displayers import Displayer, Printer
from app.formatters import ConsoleFormatter, ReverseFormatter
from app.serializers import JsonSerializer, XmlSerializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                displayer = Displayer(ConsoleFormatter())
                displayer.display(book.content)
            elif method_type == "reverse":
                displayer = Displayer(ReverseFormatter())
                displayer.display(book.content)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type == "console":
                printer = Printer(ConsoleFormatter())
                printer.print(book.title, book.content)
            elif method_type == "reverse":
                printer = Printer(ReverseFormatter())
                printer.print(book.title, book.content)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type == "json":
                serializer = JsonSerializer()
                return serializer.serialize(book.title, book.content)
            elif method_type == "xml":
                serializer = XmlSerializer()
                return serializer.serialize(book.title, book.content)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
