from app.book import Book
from app.cmd_manager.display.manager import DisplayManager
from app.cmd_manager.print.manager import PrintManager
from app.cmd_manager.serialize.manager import SerializeManager


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:

        if cmd == "display":
            displayer = DisplayManager().set_displayer(method_type)
            displayer.display(book)

        elif cmd == "print":
            printer = PrintManager().set_printer(method_type)
            printer.print_book(book)

        elif cmd == "serialize":
            serializer = SerializeManager().set_serializer(method_type)

            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
