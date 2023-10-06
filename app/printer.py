from app.book import Book


class BookPrinter:
    @staticmethod
    def print_book(book: Book, display_type: str) -> None:
        if display_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif display_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {display_type}")
