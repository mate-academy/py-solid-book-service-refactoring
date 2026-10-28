from app.mixins import DisplayMixin, PrintBookMixin, SerializeMixin


class Book(DisplayMixin, PrintBookMixin, SerializeMixin):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
