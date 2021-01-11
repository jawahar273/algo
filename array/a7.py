# Topic: Write a program to cyclically rotate an array by one.
from typing import List, Any


class Array:

    def __init__(self, elements:List[Any]) -> None:
        self.elements = elements

    def rotate(self) -> List[Any]:
        if len(self.elements) >= 2:
            last_element = self.elements.pop()
            return [last_element] + self.elements
        else:
            return self.elements

def test_a7():
    array =  Array([9, 8, 7, 6, 4, 2, 1, 3])
    assert array.rotate() == [3, 9, 8, 7, 6, 4, 2, 1]

array = Array([9, 8, 7, 6, 4, 2, 1, 3])
print(array.rotate())
