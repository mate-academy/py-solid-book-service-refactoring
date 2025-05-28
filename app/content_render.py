from abc import abstractmethod, ABC


class ContentRenderer(ABC):
    @abstractmethod
    def render(self, content: str) -> None:
        pass


class ConsoleRenderer(ContentRenderer):
    def render(self, content: str) -> None:
        print(content)


class ReverseRenderer(ContentRenderer):
    def render(self, content: str) -> None:
        print(content[::-1])
