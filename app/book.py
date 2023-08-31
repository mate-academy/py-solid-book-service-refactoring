class Book:

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def get_title(self) -> str:
        return self.title

    def get_content(self) -> str:
        return self.content
