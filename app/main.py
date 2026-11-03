from app.registry import DISPLAY_HANDLERS, PRINT_HANDLERS, SERIALIZE_HANDLERS


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
        
    def display(self, display_type: str) -> None:
        handler = DISPLAY_HANDLERS.get(display_type)
        if handler is None:
            raise ValueError(f"Unknown display type: {display_type}")
        handler(self.content)

    def print_book(self, print_type: str) -> None:
        handler = PRINT_HANDLERS.get(print_type)
        if handler is None:
            raise ValueError(f"Unknown print type: {print_type}")
        handler(self.title, self.content)

    def serialize(self, serialize_type: str) -> str:
        handler = SERIALIZE_HANDLERS.get(serialize_type)
        if handler is None:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return handler(self.title, self.content)


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
