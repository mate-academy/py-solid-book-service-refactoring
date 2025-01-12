from app.display.console import ConsoleDisplay
from app.display.reverse import ReverseDisplay
from app.print.console import ConsolePrint
from app.print.reverse import ReversePrint
from app.serialize.json import JsonSerializer
from app.serialize.xml import XmlSerializer


class Book:
    """A class representing a book with title and content."""

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
        self._operations = {
            "display": {
                "console": ConsoleDisplay(),
                "reverse": ReverseDisplay(),
            },
            "print": {
                "console": ConsolePrint(),
                "reverse": ReversePrint(),
            },
            "serialize": {
                "json": JsonSerializer(),
                "xml": XmlSerializer(),
            },
        }

    def display(self, display_type: str) -> None:
        """Display the book content using the specified display type."""
        if display_type not in self._operations["display"]:
            raise ValueError(f"Unknown display type: {display_type}")

        self._operations["display"][display_type].process(self.content)

    def print_book(self, print_type: str) -> None:
        """Print the book using the specified print type."""
        if print_type not in self._operations["print"]:
            raise ValueError(f"Unknown print type: {print_type}")

        self._operations["print"][print_type].process(self.content, self.title)

    def serialize(self, serialize_type: str) -> str:
        """Serialize the book using the specified format."""
        if serialize_type not in self._operations["serialize"]:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

        return self._operations["serialize"][serialize_type].process(
            self.content, self.title
        )


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    """Execute a series of commands on the book."""
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)

        elif cmd == "print":
            book.print_book(method_type)

        elif cmd == "serialize":
            return book.serialize(method_type)

        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
