from app.books import BookReverseJson, BookConsoleXml, Book

CMD = {
    "display": "display",
    "print": "print_book",
    "serialize": "serialize"
}

METHOD = {
    "reverse": BookReverseJson,
    "console": BookConsoleXml,
    "json": BookReverseJson,
    "xml": BookConsoleXml,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        obj = METHOD[method_type](**book.data)
        cmd = CMD[cmd]
        return getattr(obj, cmd)()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
