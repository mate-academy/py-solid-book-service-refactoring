from app.department import Display, Serialize, Print
from app.products import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            Display(method_type, book).work()
        elif cmd == "print":
            Print(method_type, book).work()
        elif cmd == "serialize":
            return Serialize(method_type, book).work()


if __name__ == "__main__":
    sample_book = Book("Sample content", "This is some sample content.")
    print(main(sample_book, [("print", "reverse")]))
    print(main(sample_book, [("display", "console"), ("serialize", "json")]))
