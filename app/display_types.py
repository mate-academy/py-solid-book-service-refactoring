from app.book import Book


class DisplayBook:
    @classmethod
    def display_book_content(cls, book: Book) -> None:
        raise ValueError("Unknown display type")


class ConsoleDisplayBook(DisplayBook):
    @classmethod
    def display_book_content(cls, book: Book) -> None:
        print(book.content)


class ReverseDisplayBook(DisplayBook):
    @classmethod
    def display_book_content(cls, book: Book) -> None:
        print(book.content[::-1])
