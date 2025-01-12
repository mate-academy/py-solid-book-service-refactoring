from app.interfaces import BookOperation


class ReversePrint(BookOperation):
    """Print reversed content with title in console."""

    def process(self, content: str, title: str | None = None) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
