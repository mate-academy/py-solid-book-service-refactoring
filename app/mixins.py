from app.serializers import SerializeJson, SerializeXml


class DisplayContent:
    def get_display_content(self, display_type: str) -> str:
        display_types = {
            "console": self.content,
            "reverse": self.content[::-1],
        }
        if display_type not in display_types:
            raise ValueError(
                f"Unknown command type: {display_type}"
            )
        return display_types[display_type]


class DisplayMixin(DisplayContent):
    def display(self, display_type: str) -> None:
        print(self.get_display_content(display_type))


class PrintBookMixin(DisplayContent):
    def print_book(self, print_type: str) -> None:
        print_types = {
            "console": f"Printing the book: {self.title}...",
            "reverse": f"Printing the book in reverse: {self.title}...",
        }
        content = self.get_display_content(print_type)
        print(print_types[print_type])
        print(content)


class SerializeMixin(SerializeJson, SerializeXml):
    def serialize(self, serialize_type: str) -> str:
        serializers = {
            "json": self.serialize_json,
            "xml": self.serialize_xml,
        }
        serializer = serializers.get(serialize_type)
        if not serializer:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return serializer()
