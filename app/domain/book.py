"""Book domain entity - pure data class following SRP."""


class Book:
    """Represents a book with title and content.

    This class has a single responsibility: holding book data.
    It does not handle display, printing, or serialization logic.
    """

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.content == other.content

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, content={self.content!r})"
