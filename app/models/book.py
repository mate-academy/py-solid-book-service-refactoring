class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, method_type: str) -> None:
        if method_type == "reverse":
            print(self.content[::-1])
        else:
            print(self.content)

    def print_book(self, method_type: str) -> None:
        if method_type == "reverse":
            print(self.content[::-1])
        else:
            print(self.content)

    def serialize(self, method_type: str) -> str:
        from app.services.serializer import JsonSerializer, XmlSerializer
        if method_type == "json":
            return JsonSerializer.serialize(self)
        elif method_type == "xml":
            return XmlSerializer.serialize(self)
        raise ValueError(f"Unknown serialize type: {method_type}")

