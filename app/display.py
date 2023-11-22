from abc import ABC, abstractmethod

from app.book import Book

class DisplayBook(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book
        
    @abstractmethod
    def display(self) -> None:
        pass
    
class ConsoleDisplayBook(DisplayBook):
    def display(self) -> None:
       print(self.content)
       

class ReverseDisplay(DisplayBook):
    def display(self) -> None:
        print(self.contenet[::-1])
    