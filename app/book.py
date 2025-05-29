class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def get_data(self) -> dict:
        return {"title": self.title, "content": self.content}
