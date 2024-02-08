from app.book import Book


class PrintBook:
    @classmethod
    def print_book(cls, book: Book) -> None:
        raise ValueError("Unknown print type")


class ConsolePrintBook(PrintBook):
    @classmethod
    def print_book(cls, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrintBook(PrintBook):
    @classmethod
    def print_book(cls, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
