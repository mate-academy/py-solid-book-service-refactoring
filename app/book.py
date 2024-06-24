class Book:
    def __init__(self, title: str, content: str) -> None:
        self._title = title
        self._content = content

    @property
    def content(self) -> str:
        return self._content

    @property
    def title(self) -> str:
        return self._title
