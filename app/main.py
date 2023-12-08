from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print import PrintConsole, PrintReverse
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            (
                DisplayReverse(book).display()
                if method_type == "reverse"
                else DisplayConsole(book).display()
            )
        elif cmd == "print":
            (
                PrintReverse(book).print()
                if method_type == "reverse"
                else PrintConsole(book).print()
            )
        elif cmd == "serialize":
            return (
                JsonSerializer(book).serialize()
                if method_type == "json"
                else XmlSerializer(book).serialize()
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
