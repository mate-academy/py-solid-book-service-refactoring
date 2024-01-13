from abc import ABC, abstractmethod


class PrintService(ABC):
    @abstractmethod
    def print(self):
        pass


