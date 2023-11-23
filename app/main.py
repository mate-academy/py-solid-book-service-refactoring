from app.book import Book
from app.book_print import BookPrint
from app.book_display import BookDisplay
from app.book_serialize import BookSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    results = ""
    for cmd, method_type in commands:
        if cmd == "display":
            processor = BookDisplay(book)
        elif cmd == "print":
            processor = BookPrint(book)
        elif cmd == "serialize":
            processor = BookSerialize(book)
        else:
            raise ValueError("Unknown command type.")

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


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
