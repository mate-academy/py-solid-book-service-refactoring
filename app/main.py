from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JSONSerializer, XMLSerializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                displayer = ConsoleDisplayer()
            elif method_type == "reverse":
                displayer = ReverseDisplayer()
            else:
                raise ValueError(f"Unknown display type: {method_type}")

            displayer.display(book)

        elif cmd == "print":
            if method_type == "console":
                printer = ConsolePrinter()
            elif method_type == "reverse":
                printer = ReversePrinter()
            else:
                raise ValueError(f"Unknown print type: {method_type}")

            printer.print(book)

        elif cmd == "serialize":
            if method_type == "json":
                serializer = JSONSerializer()
            elif method_type == "xml":
                serializer = XMLSerializer()
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(book)

        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "console"), ("display", "reverse")]))
    print("-" * 30)
    print(main(sample_book, [("print", "console"), ("print", "reverse")]))
    print("-" * 30)
    print(main(sample_book, [("serialize", "json"), ("serialize", "xml")]))
