class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        if display_type == "console":
            print(self.content)
            return
        elif display_type == "reverse":
            print(self.content[::-1])
            return
        raise ValueError(f"Unknown display type: {display_type}")
