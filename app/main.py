from app.books import Book
from app.console_commands import COMMAND_MAP


def main(book: Book, commands: list[tuple[str, str]]) -> None:
    for cmd, method_type in commands:
        handler_map, handler_class = COMMAND_MAP[cmd]
        handler = handler_class(handler_map[method_type])
        handler_class_method = getattr(handler, cmd)
        if handler_class_method:
            return handler_class_method(book)


if __name__ == "__main__":
    sample_book = Book(
        title="Sample Book",
        content="This is some sample content.",
    )
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
