from app.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for command, method in commands:
        return book.handle(command, method)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
