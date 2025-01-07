from app.classes import Book, BookDisplay, PrintBook, BookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            BookDisplay.display(display_type=method_type, book=book)
        elif cmd == "print":
            PrintBook.print_book(print_type=method_type, book=book)
        elif cmd == "serialize":
            return BookSerializer.serialize(serialize_type=method_type, book=book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
