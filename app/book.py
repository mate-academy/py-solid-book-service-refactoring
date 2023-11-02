class Book:
    def __init__(self, title: str, content: str) -> None:
        # I would love to add encapsulation here,
        # but since the tests are not passing,
        # I have left only the methods to get.
        self.title = title
        self.content = content

    def get_title(self) -> str:
        return self.title

    def get_content(self) -> str:
        return self.content
