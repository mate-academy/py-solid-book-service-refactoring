class Displayer:
    def __init__(self, book):
        self.book = book

    def display_console(self):
        print(self.book.content)

    def display_reverse(self):
        print(self.book.content[::-1])

    def display(self, method_type: str):
        method_name = f"display_{method_type}"
        method = getattr(self, method_name, None)

        if not callable(method):
            raise ValueError(f"Unknown display method: {method_type}")

        method()