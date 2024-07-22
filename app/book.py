from app.strateges import Display, Print, Serialize


class Book:
    strategy = {
        "display": {
            "console": Display.console,
            "reverse": Display.reverse
        },
        "print": {
            "console": Print.console,
            "reverse": Print.reverse
        },
        "serialize": {
            "json": Serialize.json,
            "xml": Serialize.xml
        }
    }

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        display_strategy = self.strategy["display"].get(display_type)
        if not display_strategy:
            raise ValueError(f"Unknown display type: {display_type}")
        display_strategy(self.content)

    def print_book(self, print_type: str) -> None:
        print_strategy = self.strategy["print"].get(print_type)
        if not print_strategy:
            raise ValueError(f"Unknown print type: {print_type}")
        print_strategy(self.title, self.content)

    def serialize(self, serialize_type: str) -> str:
        serialize_strategy = self.strategy["serialize"].get(serialize_type)
        if not serialize_strategy:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return serialize_strategy(self.title, self.content)
