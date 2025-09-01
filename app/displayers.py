from app.models import Book


class ConsoleDisplayer:
    """Displays book content to the console."""
    def display(self, book: Book) -> None:
        """Print the book content as-is."""
        print(book.content)


class ReverseDisplayer:
    """Displays book content in reverse order."""
    def display(self, book: Book) -> None:
        """Print the book content reversed."""
        print(book.content[::-1])
