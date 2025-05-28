from typing import Optional

from app.book import Book, JsonSerializer, XmlSerializer
from app.content_render import ConsoleRenderer, ReverseRenderer


def main(book: Book, commands: list[tuple[str, str]]) -> Optional[str]:
    for cmd, method_type in commands:
        match cmd:
            case "display":
                if method_type == "console":
                    book.display(ConsoleRenderer())
                elif method_type == "reverse":
                    book.display(ReverseRenderer())
            case "print":
                if method_type == "console":
                    book.print_book(ConsoleRenderer())
                elif method_type == "reverse":
                    book.print_book(ReverseRenderer())
            case "serialize":
                if method_type == "json":
                    return JsonSerializer().serialize(book)
                elif method_type == "xml":
                    return XmlSerializer().serialize(book)
                else:
                    raise ValueError(f"Unknown method type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
