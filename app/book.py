class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def __str__(self) -> str:
        return self.title
