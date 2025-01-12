from app.interfaces import BookOperation


class ReverseDisplay(BookOperation):
    """Display content in reverse order in console."""

    def process(self, content: str, title: str | None = None) -> None:
        print(content[::-1])
