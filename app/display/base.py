from abc import abstractmethod, ABC


class BaseDisplayHandler(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass
