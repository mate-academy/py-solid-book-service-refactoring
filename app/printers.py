from abc import ABC, abstractmethod

from app.publications import Publication


class BasePrinter(ABC):
    @abstractmethod
    def print(self, publication: Publication) -> None:
        pass


class ConsolePrinter(BasePrinter):
    def print(self, publication: Publication) -> None:
        print(
            f"Printing the {publication.type_name()}: {publication.title}..."
        )
        print(publication.content)


class ReversePrinter(BasePrinter):
    def print(self, publication: Publication) -> None:
        print(
            f"Printing the {publication.type_name()} in reverse: "
            f"{publication.title}..."
        )
        print(publication.content[::-1])
