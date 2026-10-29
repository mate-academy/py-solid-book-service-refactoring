class Book:
    """Represents a book with title and content."""

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def __str__(self) -> str:
        return f"Book(title='{self.title}', content='{self.content}')"
