class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Info:
    @staticmethod
    def console(book: Book) -> None:
        print(book.content)

    @staticmethod
    def reverse(book: Book) -> None:
        print(book.content[::-1])
