from app.display import ConsoleBookDisplay, ReverseBookDisplay
from app.serializer import JsonBookSerializer, XmlBookSerializer
from app.print import ConsoleBookPrint, ReverseBookPrint


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: "Book", commands: list[tuple[str, str]]) -> None | str:
    # Dictionary mapping commands to methods
    command_methods = {
        "display": {
            "console": ConsoleBookDisplay(book).display,
            "reverse": ReverseBookDisplay(book).display
        },
        "print": {
            "console": ConsoleBookPrint(book).print,
            "reverse": ReverseBookPrint(book).print
        },
        "serialize": {
            "json": JsonBookSerializer(book).serialize,
            "xml": XmlBookSerializer(book).serialize
        }
    }

    for cmd, method_type in commands:
        if cmd in command_methods and method_type in command_methods[cmd]:
            method_to_call = command_methods[cmd][method_type]
            if cmd == "serialize":
                return method_to_call()
            method_to_call()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
