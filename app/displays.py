from abc import ABC, abstractmethod

from app.publications import Publication


class BaseDisplay(ABC):
    @abstractmethod
    def display(self, publication: Publication) -> None:
        pass


class ConsoleDisplay(BaseDisplay):
    def display(self, publication: Publication) -> None:
        print(publication.content)


class ReverseDisplay(BaseDisplay):
    def display(self, publication: Publication) -> None:
        print(publication.content[::-1])
