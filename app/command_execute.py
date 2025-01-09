from abc import ABC, abstractmethod


class CommandExecute(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
