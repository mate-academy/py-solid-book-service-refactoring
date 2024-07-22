class PrintConsole:
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)

    def __call__(self, *args, **kwargs) -> None:
        self.print_book(*args, **kwargs)


class PrintReverse:
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content[::-1])

    def __call__(self, *args, **kwargs) -> None:
        self.print_book(*args, **kwargs)
