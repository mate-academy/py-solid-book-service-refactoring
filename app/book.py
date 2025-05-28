from abc import ABC
from dataclasses import dataclass


@dataclass
class Book(ABC):
    title: str
    content: str
