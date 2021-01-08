# Topic: Find the maximum and minimum element in an array
from typing import List, Any


class MinMax:
    def __init__(self, elements: List[Any]) -> None:
        self.elements = elements

    def min(self) -> Any:
        return min(self.elements)

    def min_loop(self) -> Any:
        temp = self.elements[0]
        for element in self.elements:
            if temp > element:
                temp = element
        return temp

    def max_loop(self) -> Any:
        temp = self.elements[0]
        for element in self.elements:
            if temp < element:
                temp = element
        return temp

    def max(self) -> Any:
        return max(self.elements)


def test_a2():
    elements = [1, 3, 4, 5, 6, 9, 100, 10]
    __array = MinMax(elements)
    assert __array.elements == elements
    assert __array.min() == 1
    assert __array.max() == 100

    assert __array.min_loop() == 1
    assert __array.max_loop() == 100



__array = MinMax([1000, 12, 45, 56, 1990, 1])
print(__array.max())
print(__array.min())
print(__array.min_loop())
print(__array.max_loop())
