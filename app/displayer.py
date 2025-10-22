from app.interfaces.book_display_interface import BookDisplayInterface


class ConsoleBookDisplay(BookDisplayInterface):
    @staticmethod
    def display(book: "Book") -> None:
        print(book.content)

class ReverseBookDisplay(BookDisplayInterface):
    @staticmethod
    def display(book: "Book") -> None:
        print(book.content[::-1])
