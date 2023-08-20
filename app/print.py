from app.book import Book, Info


class Print:
    @staticmethod
    def print_book(book: Book, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {book.title}...")
            Info.console(book)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            Info.reverse(book)
        else:
            raise ValueError(f"Unknown print type: {print_type}")
