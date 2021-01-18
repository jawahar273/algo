# Topic: find duplicate in an array of N+1 Integers

from typing import Dict, List, Any
from collections import defaultdict

class Array:

    def __init__(self, elements: List[Any]) -> None:
        self.elements = elements
        assert len(self.elements) > 0 , "List can not empty"

    def find_duplicate(self):
        count: Dict[int, int] = defaultdict(int)
        for el in self.elements:
            count[el] += 1
        return sorted(count.items(), key=lambda item: item[1])[-1][0]
        

array = Array([1,3,4,2,2])

print("List: ", array.elements)
print("Find the Duplicate Number: ", array.find_duplicate())

def test_a11():
    array = Array([3,1,3,4,2])
    assert array.find_duplicate() == 3
