class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display_console(self) -> None:
        print(self.content)

    def display_reverse(self) -> None:
        print(self.content[::-1])

    def display(self, method_type: str) -> None:
        if method_type == "reverse":
            self.display_reverse()
        elif method_type == "console":
            self.display_console()
