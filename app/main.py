from app.models import Book, ConsoleBook, ReverseBook
from app.serializers import Json, Xml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if method_type == "console":
            book = ConsoleBook(book.title, book.content)
        elif method_type == "reverse":
            book = ReverseBook(book.title, book.content)
        if cmd == "display":
            book.display()
        elif cmd == "print":
            book.print_book()
        elif cmd == "serialize":
            if method_type == "json":
                return Json.serialize(book)
            elif method_type == "xml":
                return Xml.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
