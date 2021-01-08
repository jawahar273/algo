# Topic: Reverse the array
from typing import List, Any


class Array: 
    def __init__(self, elements: List[Any]) -> None:
        self.elements = elements

    def reverse(self) -> List[Any]:
        self.elements = self.elements[::-1]
        return self.elements

    def reverse_loop(self) -> List[Any]:
        start = 0
        end = len(self.elements) - 1
        while start < end:
            self.elements[start], self.elements[end] = self.elements[end], self.elements[start]
            start += 1
            end -= 1
        return self.elements
    
    def display(self):
        print("Element display", self.elements)

def test_a1():
    elements = [12, 34, 45, 56, 78]
    __array = Array(elements)
    assert __array.elements == elements

    assert __array.reverse() == elements[::-1]

    assert __array.reverse_loop() == elements


__array = Array([1, 2, 3, 4, 5, 6])
__array.display()
__array.reverse()
__array.display()
__array.reverse_loop()
__array.display()
