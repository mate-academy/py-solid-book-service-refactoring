from app.displays import ConsoleDisplay, ReverseDisplay, Display
from app.prints import ConsolePrint, ReversePrint, Print
from app.serializers import JsonSerializer, XmlSerializer, Serializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.__title = title
        self.__content = content

    @property
    def title(self) -> str:
        return self.__title

    @property
    def content(self) -> str:
        return self.__content

    def display(self, method: Display) -> None:
        method.display(self.content)

    def print_book(self, method: Print) -> None:
        method.print(self.title, self.content)

    def serialize(self, method: Serializer) -> str:
        return method.serialize(self.title, self.content)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_types = {
        "display_console": ConsoleDisplay(),
        "display_reverse": ReverseDisplay(),
        "print_console": ConsolePrint(),
        "print_reverse": ReversePrint(),
        "serialize_json": JsonSerializer(),
        "serialize_xml": XmlSerializer(),
    }

    for cmd, method_type in commands:
        method = display_types.get(f"{cmd}_{method_type}")

        if cmd == "display":
            book.display(method)
        elif cmd == "print":
            book.print_book(method)
        elif cmd == "serialize":
            return book.serialize(method)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
    print(
        main(
            sample_book,
            [
                ("display", "reverse"),
                ("print", "console"),
                ("serialize", "xml")
            ]
        )
    )
