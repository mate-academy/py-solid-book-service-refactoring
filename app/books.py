class Book:

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Base:

    def __init__(self, book: Book) -> None:
        self.book = book
