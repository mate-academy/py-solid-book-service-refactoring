from app.book import Book, DisplayHandler, PrintHandler, SerializeHandler


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None
    for cmd, method_type in commands:
        if cmd == "display":
            DisplayHandler.execute(book, method_type)
        elif cmd == "print":
            PrintHandler.execute(book, method_type)
        elif cmd == "serialize":
            result = SerializeHandler.execute(book, method_type)
        else:
            raise ValueError(f"Unknown command: {cmd}")
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
