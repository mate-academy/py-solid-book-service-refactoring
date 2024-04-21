from abc import ABC, abstractmethod


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return f'{{"title": "{title}", "content": "{content}"}}'


class XmlSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return f"<title>{title}</title>\n<content>{content}</content>"
