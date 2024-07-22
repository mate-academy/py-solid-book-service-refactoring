class DisplayConsole:
    def display(self, title: str, content: str) -> None:
        print(content)

    def __call__(self, *args, **kwargs) -> None:
        self.display(*args, **kwargs)


class DisplayReverse:
    def display(self, title: str, content: str) -> None:
        print(content[::-1])

    def __call__(self, *args, **kwargs) -> None:
        self.display(*args, **kwargs)
