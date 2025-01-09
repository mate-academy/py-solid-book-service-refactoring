class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def __str__(self) -> str:
        return self.title

    @staticmethod
    def validate_book(title: str, content: str) -> None:
        if not title or not content:
            raise ValueError(
                "Both title and content must be provided and non-empty."
            )

    def save(self) -> "Book":
        self.validate_book(self.title, self.content)
        return self
