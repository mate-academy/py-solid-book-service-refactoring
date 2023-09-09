from app.book import Book
from app.printer import SimplePrinter
from app.screen import SimpleScreen
from app.serializer import SerializerFactory


def display_content(method_type: str, book: Book) -> None:
    screen = SimpleScreen(method_type, book)
    screen.display()


def print_content(method_type: str, book: Book) -> None:
    printer = SimplePrinter(method_type, book)
    printer.print()


def serialize_content(method_type: str, book: Book) -> str:
    serializer = SerializerFactory(method_type, book)
    serializer = serializer.create_serializer()
    return serializer.serialize()


def dispatch_command(cmd: str, method_type: str, book: Book) -> None | str:
    if cmd == "display":
        display_content(method_type, book)
    elif cmd == "print":
        print_content(method_type, book)
    elif cmd == "serialize":
        return serialize_content(method_type, book)
    else:
        raise NotImplementedError(f"Command {cmd} is not implemented")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        return dispatch_command(cmd, method_type, book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(
        main(
            sample_book, [
                ("print", "console"),
                ("serialize", "xml")
            ]
        )
    )
