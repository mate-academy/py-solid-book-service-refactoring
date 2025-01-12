from app.interfaces import BookOperation


class ConsolePrint(BookOperation):
    """Print content with title in console."""

    def process(self, content: str, title: str | None = None) -> None:
        print(f"Printing the book: {title}...")
        print(content)
