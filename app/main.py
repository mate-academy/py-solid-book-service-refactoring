from app.book import Book, Display, Print
from app.serializer import SerializeToJSON, SerializeToXML


class DisplayConsole(Display):
    def display_book(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(Display):
    def display_book(self, book: Book) -> None:
        print(book.content[::-1])


class PrintConsole(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {
        "console": DisplayConsole(),
        "reverse": DisplayReverse()
    }
    printers = {
        "console": PrintConsole(),
        "reverse": PrintReverse()
    }
    serializers = {
        "json": SerializeToJSON(),
        "xml": SerializeToXML()
    }
    for cmd, method_type in commands:
        if cmd == "display":
            display = displays.get(method_type)
            return display.display_book(book)
        elif cmd == "print":
            printer = printers.get(method_type)
            return printer.print_book(book)
        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            return serializer.serialize_book(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "XML")]))
