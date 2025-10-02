class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self) -> None:
        print(self.content)

    def display_reverse(self) -> None:
        print(self.content[::-1])

    def print_book(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def reverse_print_book(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
