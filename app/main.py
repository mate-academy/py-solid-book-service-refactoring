from app.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    actions = {
        "display": book.display,
        "print": book.print_book,
        "serialize": book.serialize,
    }
    for cmd, method_type in commands:
        action = actions.get(cmd)
        if action is None:
            continue
        result = action(method_type)
        if result is not None:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
