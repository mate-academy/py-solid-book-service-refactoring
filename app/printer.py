from app.book import Book


class BookPrinter:
    @staticmethod
    def print_book(book: Book, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {book.title}...\n{book.content}")
            return
        elif print_type == "reverse":
            print(f"Printing the book in reverse: "
                  f"{book.title}...\n{book.content[::-1]}")
            return
        raise ValueError(f"Unknown print type: {print_type}")
