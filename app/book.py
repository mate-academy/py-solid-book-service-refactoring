class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def get_context(self, *args) -> dict:
        return {"heading": self.title, "text": self.content}
