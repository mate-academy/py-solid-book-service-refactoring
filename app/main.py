from app.serializer import Serializer
from app.book import Book
from app.display import Display
from app.printer import Printer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display = Display.get_display_class(method_type)
            display().display(book.content)

        elif cmd == "print":
            printer = Printer.get_printer_class(method_type)
            printer().print(book)

        elif cmd == "serialize":
            serializer = Serializer.get_serializer_class(method_type)
            return serializer().serialize(book=book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
