class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookReverse:

    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])

    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class BookConsole:

    @staticmethod
    def display(book: Book) -> None:
        print(book.content)

    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)
