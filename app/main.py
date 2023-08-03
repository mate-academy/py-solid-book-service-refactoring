from app.book import Book, DisplayBook, PrintBook, SerializeBook


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DisplayBook(method_type).display_book_info(book)
        elif cmd == "print":
            PrintBook(method_type).display_book_info(book)
        elif cmd == "serialize":
            return SerializeBook(method_type).display_book_info(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
