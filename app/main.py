from app.handlers import get_handler, DISPLAYS, PRINTERS, SERIALIZERS
from app.models import Book


def main(book: Book, commands: list) -> None | str:
    for cmd, method_type in commands:
        match cmd:
            case "display":
                get_handler(DISPLAYS, method_type, cmd).display(book)
            case "print":
                get_handler(PRINTERS, method_type, cmd).print(book)
            case "serialize":
                return get_handler(SERIALIZERS, method_type, cmd).serialize(
                    book,
                )
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
