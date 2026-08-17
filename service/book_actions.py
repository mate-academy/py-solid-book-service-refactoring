# services/book_actions.py
from typing import Protocol, Any

# Створюємо протоколи (інтерфейси), щоб дотриматись DIP
class Repository(Protocol):
    def save(self, data: dict[str, Any]) -> Any: ...

class Notifier(Protocol):
    def send(self, message: str) -> None: ...

class BookService:
    """Сервіс для керування логікою книг."""

    def __init__(self, repository: Repository, notifier: Notifier) -> None:
        self.repository = repository
        self.notifier = notifier

    def create_book(self, data: dict[str, Any]) -> Any:
        book = self.repository.save(data)
        # Переконайтеся, що об'єкт 'book' має атрибут .title, як і в оригіналі
        self.notifier.send(f"Книга '{book.title}' додана успішно!")
        return book
