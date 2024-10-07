from app.display import ConsoleDisplay, ReverseDisplay, Display
from app.print import ConsolePrinter, ReversePrinter, Printer
from app.serializers import JsonSerializer, XmlSerializer, Serializer


class Book:
    def __init__(
            self,
            title: str,
            content: str,
    ) -> None:
        self.title = title
        self.content = content

    def display(self, display_service: Display) -> None:
        display_service.display(self.content)

    def print_book(self, printer_service: Printer) -> None:
        printer_service.print(self.title, self.content)

    def serialize(self, serializer_service: Serializer) -> str:
        return serializer_service.serialize(self.title, self.content)


def main(
        book: Book,
        commands: list[tuple[str, str]],
) -> None | str:
    for cmd, method_type in commands:
        try:
            if cmd == "display":
                if method_type == "console":
                    book.display(ConsoleDisplay())
                elif method_type == "reverse":
                    book.display(ReverseDisplay())
                else:
                    raise ValueError(f"Unknown display type: {method_type}")
            elif cmd == "print":
                if method_type == "console":
                    book.print_book(ConsolePrinter())
                elif method_type == "reverse":
                    book.print_book(ReversePrinter())
                else:
                    raise ValueError(f"Unknown printer type: {method_type}")
            elif cmd == "serialize":
                if method_type == "json":
                    return book.serialize(JsonSerializer())
                elif method_type == "xml":
                    return book.serialize(XmlSerializer())
                else:
                    raise ValueError(
                        f"Unknown serialization type: {method_type}"
                    )
            else:
                raise ValueError(f"Unknown command: {cmd}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    result = main(sample_book, [("display", "reverse"), ("serialize", "xml")])
    if result:
        print(result)
