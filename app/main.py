from .book import Book
from .display import BookDisplay
from .print import BookPrint
from .serialize import BookSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    method_mapping = {
        ("display", "console"): BookDisplay().console,
        ("display", "reverse"): BookDisplay().reverse,
        ("print", "console"): BookPrint().console,
        ("print", "reverse"): BookPrint().reverse,
        ("serialize", "json"): BookSerialize().json,
        ("serialize", "xml"): BookSerialize().xml,
    }

    for cmd, method_type in commands:
        if (cmd, method_type) in method_mapping:
            method = method_mapping[(cmd, method_type)]
            return method(book) if cmd == "serialize" else method(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
