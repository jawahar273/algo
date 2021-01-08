# Topic: Move all the negative elements to one side of the array 
from typing import List, Any

class Array:

    def __init__(self, elements: List[Any]) -> None:
        self.elements = elements

    def sort(self) -> List[Any]:
        print(self.elements)
        return sorted(self.elements)


__array = Array([-12, 11, -13, -5, 6, -7, 5, -3, -6])
print("Move all the negative elements to one side of the array: ", __array.sort())


