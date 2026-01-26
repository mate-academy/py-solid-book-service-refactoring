from typing import List, Tuple, Optional, Dict
from app.book import Book
from app.interfaces import (IDisplayStrategy,
                            IPrintStrategy,
                            ISerializerStrategy)


class BookService:
    def __init__(self,
                 display_strategies: Dict[str, IDisplayStrategy],
                 print_strategies: Dict[str, IPrintStrategy],
                 serialize_strategies: Dict[str, ISerializerStrategy]) -> None:
        self.display_strategies = display_strategies
        self.print_strategies = print_strategies
        self.serialize_strategies = serialize_strategies

    def process(self,
                book: Book,
                commands: List[Tuple[str, str]]
                ) -> Optional[str]:
        for cmd, method_type in commands:
            if cmd == "display":
                strategy = self.display_strategies.get(method_type)
                if strategy:
                    strategy.display(book)
                else:
                    raise ValueError(f"Unknown display strategy: "
                                     f"{method_type}")

            elif cmd == "print":
                strategy = self.print_strategies.get(method_type)
                if strategy:
                    strategy.print_book(book)
                else:
                    raise ValueError(f"Unknown print strategy: "
                                     f"{method_type}")

            elif cmd == "serialize":
                strategy = self.serialize_strategies.get(method_type)
                if strategy:
                    return strategy.serialize(book)
                else:
                    raise ValueError(f"Unknown serialize strategy: "
                                     f"{method_type}")

        return None
