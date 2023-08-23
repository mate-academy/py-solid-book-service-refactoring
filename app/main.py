from app.book_management.display import ConsoleDisplay, ReverseDisplay
from app.book_info.book import Book
from app.book_management.print_book import ConsolePrint, ReversePrint
from app.book_management.serialize import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayers = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }
    printers = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }
    serializers = {
        "json": JsonSerialize(),
        "xml": XmlSerialize(),
    }
    for cmd, method_type in commands:
        if cmd == "display":
            displayers[method_type].display(book.content)
        elif cmd == "print":
            printers[method_type].print_book(book.title, book.content)
        elif cmd == "serialize":
            return serializers[method_type].serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
