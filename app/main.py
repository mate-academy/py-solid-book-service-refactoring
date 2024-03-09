from app.display import ConsoleBookDisplay, ReverseBookDisplay
from app.serializer import JsonBookSerializer, XmlBookSerializer
from app.print import ConsoleBookPrint, ReverseBookPrint


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleBookDisplay(book).display()
            elif method_type == "reverse":
                ReverseBookDisplay(book).display()
        elif cmd == "print":
            if method_type == "console":
                ConsoleBookPrint(book).print()
            elif method_type == "reverse":
                ReverseBookPrint(book).print()
        elif cmd == "serialize":
            if method_type == "json":
                return JsonBookSerializer(book).serialize()
            elif method_type == "xml":
                return XmlBookSerializer(book).serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
