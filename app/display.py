class DisplayStrategy:
    def display(self, book) -> None:
        raise NotImplementedError


class ConsoleDisplay(DisplayStrategy):
    def display(self, book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book) -> None:
        print(book.content[::-1])
