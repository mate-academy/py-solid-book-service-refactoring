from app.models import Book


class DisplayService:
    def __init__(self) -> None:
        pass

    def console(self, book: Book) -> None:
        print(book.content)

    def reverse(self, book: Book) -> None:
        print(book.content[::-1])


class PrintService(DisplayService):

    def console(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        super().console(book)

    def reverse(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        super().reverse(book)
