from abc import abstractmethod, ABC


class Print(ABC):
    @abstractmethod
    def print_entity(self, name: str, title_: str, content_: str) -> None:
        pass


class ConsolePrint(Print):
    def print_entity(self, name: str, title_: str, content_: str) -> None:
        print(f"Printing the {name}: {title_}...")
        print(content_)


class ReversePrint(Print):
    def print_entity(self, name: str, title_: str, content_: str) -> None:
        print(f"Printing the {name} in reverse: "
              f"{title_}...")
        print(content_[::-1])
