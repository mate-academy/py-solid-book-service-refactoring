class PrintConsole:
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)

    def __call__(self, *args, **kwargs) -> None:
        self.print(*args, **kwargs)


class PrintReverse:
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])

    def __call__(self, *args, **kwargs) -> None:
        self.print(*args, **kwargs)
