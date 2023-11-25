from app.book import Book
from app.book_print import BookPrint
from app.book_display import BookDisplay
from app.book_serialize import BookSerialize


def process_command(book: Book, cmd: str, method_type: str) -> str:
    results = ""
    processors = {
        "display": BookDisplay,
        "print": BookPrint,
        "serialize": BookSerialize,
    }

    if cmd not in processors:
        raise ValueError("Unknown command type.")

    processor = processors[cmd](book)

    if hasattr(processor, method_type):
        method = getattr(processor, method_type)
        if cmd == "serialize":
            result = method()
            print(result)
            results += result
        else:
            method()
    else:
        raise ValueError(f"Unknown {cmd} type.")
    return results


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        return process_command(book, cmd, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
