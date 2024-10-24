from app.display import get_display_class
from app.print import get_print_class
from app.serialize import get_serialize_class


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_method = get_display_class(method_type)
            display_method.display(book.content)
        elif cmd == "print":
            print_method = get_print_class(method_type)
            print_method.print_info(book.title, book.content)
        elif cmd == "serialize":
            serialize_method = get_serialize_class(method_type)
            return serialize_method.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
