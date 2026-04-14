from app.serializer import JsonSerializer, XmlSerializer
from app.printer import ConsolePrinter, ReversePrinter
from app.display import Console, Reverse


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        displays = {
            "console": Console(),
            "reverse": Reverse(),
        }

        if display_type not in displays:
            raise ValueError(f"Unknown print type: {display_type}")

        displays[display_type].display(self)

    def print_book(self, print_type: str) -> None:
        printers = {
            "console": ConsolePrinter(),
            "reverse": ReversePrinter(),
        }
        if print_type not in printers:
            raise ValueError(f"Unknown print type: {print_type}")

        printers[print_type].print_book(self)

    def serialize(self, serialize_type: str) -> str:
        serializers = {
            "json": JsonSerializer(),
            "xml": XmlSerializer(),
        }

        if serialize_type not in serializers:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

        return serializers[serialize_type].serialize(self)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
