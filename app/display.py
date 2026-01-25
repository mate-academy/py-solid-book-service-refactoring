from app.interfaces import HasContent


class DisplayStrategy:
    def display(self, book: HasContent) -> None:
        raise NotImplementedError


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: HasContent) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: HasContent) -> None:
        print(book.content[::-1])
