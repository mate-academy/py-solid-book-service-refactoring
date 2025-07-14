from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.models import Book
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JSONSerializer, XMLSerializer


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
