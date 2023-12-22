from app.managers import DisplayManager, PrintManager, SerializeManager


class Book(DisplayManager, PrintManager, SerializeManager):
    def __init__(self, title: str, content: str) -> None:
        DisplayManager.__init__(self, content)
        PrintManager.__init__(self, title, content)
        SerializeManager.__init__(self, self)
        self.title = title
        self.content = content
