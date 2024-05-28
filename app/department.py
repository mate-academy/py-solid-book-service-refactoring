import json
import xml.etree.ElementTree as ET  # noqa: N817
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class MainDepart(ABC):
    def __init__(self, method: str = None, product: str = None) -> None:
        self._method = method
        self._product = product

    @abstractmethod
    def no_such_method(self) -> None:
        pass

    @abstractproperty
    def WHAT_WE_DO(self) -> None:  # noqa: N802
        pass

    def work(self) -> None:
        if not self.WHAT_WE_DO.get(self.method, False):
            self.no_such_method()
        else:
            return eval(self.WHAT_WE_DO.get(self.method))

    @property
    def method(self) -> None:
        return self._method

    @method.setter
    def method(self, value: Any) -> None:
        raise AttributeError("Denied")

    @property
    def product(self) -> None:
        return self._product

    @product.setter
    def product(self, value: Any) -> None:
        raise AttributeError("Denied")

    def no_such_method(self) -> None:  # noqa: F811
        raise ValueError(f"Default error for department, "
                         f"which don`t have own error "
                         f"in method: {self.method}")


class Display(MainDepart):
    def __init__(self, method: str, product: str) -> None:
        super().__init__(method, product)

    WHAT_WE_DO = {"console": "self.display_console()",
                  "reverse": "self.display_reverse()"}

    def display_console(self) -> None:
        print(self.product.content)

    def display_reverse(self) -> None:
        print(self.product.content[::-1])

    def no_such_method(self) -> None:
        raise ValueError(f"Unknown display type: {self.method}")


class Print(MainDepart):
    def __init__(self, method: str, product: str) -> None:
        super().__init__(method, product)

    WHAT_WE_DO = {"console": "self.print_console()",
                  "reverse": "self.print_reverse()"}

    def print_console(self) -> None:
        print(f"Printing the book: {self.product.title}...")
        print(self.product.content)

    def print_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.product.title}...")
        print(self.product.content[::-1])

    def no_such_method(self) -> None:
        raise ValueError(f"Unknown print type: {self.method}")


class Serialize(MainDepart):
    def __init__(self, method: str, product: str) -> None:
        super().__init__(method, product)

    WHAT_WE_DO = {"json": "self.serialize_json()",
                  "xml": "self.serialize_xml()"}

    def serialize_json(self) -> None:
        return json.dumps(
            {
                "title": self.product.title,
                "content": self.product.content
            }
        )

    def serialize_xml(self) -> None:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.product.title
        content = ET.SubElement(root, "content")
        content.text = self.product.content
        return ET.tostring(root, encoding="unicode")

    def no_such_method(self) -> None:
        raise ValueError(f"Unknown serialize type: {self.method}")
