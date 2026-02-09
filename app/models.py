class Book:
    __slots__ = ("title", "content")

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
