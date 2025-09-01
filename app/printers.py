from app.models import Book


class ConsolePrinter:
    """Prints book content to the console."""
    def print(self, book: Book) -> None:
        """Print the book content as-is, with a title header."""
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter:
    """Prints book content in reverse order."""
    def print(self, book: Book) -> None:
        """Print the book content reversed, with a title header."""
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
