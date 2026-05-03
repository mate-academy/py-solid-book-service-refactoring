from app.interfaces import BookInterface


class Book(BookInterface):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
