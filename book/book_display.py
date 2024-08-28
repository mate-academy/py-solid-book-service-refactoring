from book.book import Book


class DisplayBook(Book):
    def __init__(self, book: Book) -> None:
        super().__init__(title=book.title, content=book.content)

    def display_console(self) -> None:
        print(self.content)

    def display_reverse(self) -> None:
        print(self.content[::-1])
