class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def print_content(self) -> None:
        print(self.content)

    def print_content_reverse(self) -> None:
        print(self.content[::-1])
