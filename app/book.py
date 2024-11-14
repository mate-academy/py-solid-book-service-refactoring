class Book:
    def __init__(self, title: str, content: str) -> None:
        self._title = title
        self._content = content

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, new_title: str) -> None:
        self._title = new_title

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, new_content: str) -> None:
        self._content = new_content
