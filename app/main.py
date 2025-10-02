from app.books import Book
from app.mappers import COMMANDS_MAPPER


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd not in COMMANDS_MAPPER:
            raise ValueError(f"Unknown command: {cmd}")
        method_mapper = COMMANDS_MAPPER[cmd]
        if method_type not in method_mapper:
            raise ValueError(f"Unknown {cmd} method: {method_type}")
        output = method_mapper[method_type]()
        result = getattr(output, cmd)(book)
        if cmd == "serialize":
            return result
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
