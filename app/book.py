class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def print_content(self):
        print(self.content)

    def print_content_reverse(self):
        print(self.content[::-1])
