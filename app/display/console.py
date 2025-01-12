from app.interfaces import BookOperation


class ConsoleDisplay(BookOperation):
    """Display content in console."""

    def process(self, content: str, title: str | None = None) -> None:
        print(content)
