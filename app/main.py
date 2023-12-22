from .managers import DisplayManager, PrintManager, SerializeManager


class Book(DisplayManager, PrintManager, SerializeManager):
    def __init__(self, title: str, content: str) -> None:
        DisplayManager.__init__(self, content)
        PrintManager.__init__(self, title, content)
        SerializeManager.__init__(self, self)
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
