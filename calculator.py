from typing import Union

class Calculator:

    def __init__(self) -> None:
        pass

    def add(self, x: int, y: int) -> int:
        return x+y

    def multiply(self, x: int, y: int) -> int:
        return x*y

    def divide(self, x: int, y: int) -> Union[int, float]:
        return x / y

    def subtract(self, x: int, y: int) -> int:
        return x - y

    