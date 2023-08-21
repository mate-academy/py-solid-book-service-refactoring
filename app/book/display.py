from app.book.book import Book


class Display:
    def __init__(self, display_type: str) -> None:
        self._display_type = display_type

    @property
    def display_type(self) -> str:
        return self._display_type

    @display_type.setter
    def display_type(self, display_type: str) -> [None | ValueError]:
        if display_type in ("console", "reverse"):
            self._display_type = display_type
        else:
            ValueError(f"Unknown display type: {display_type}")

    def show_content(self, book: Book) -> None:
        content = (
            book.content[::-1]
            if self.display_type != "console"
            else book.content
        )

        print(content)


def display_book(book: Book, display_type: str) -> None:
    display = Display(display_type)
    display.show_content(book)
