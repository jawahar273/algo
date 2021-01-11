# Topic:  find Largest sum contiguous Subarray 
from typing import List, Any


class Array:

    def __init__(self, elements: List[Any]) -> None:
        self.elements = elements

    def sub_max(self):
        _max = self.elements[0]
        max_now = self.elements[0]

        for element in self.elements[1:]:
            max_now = max(element, max_now + element)
            _max = max(max_now, _max)
        return _max


array = Array([1, 2, 3, -2, 5])
print(array.sub_max())


def test_a8():
    array = Array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert 6 == array.sub_max()

    array = Array([1, 2, 3, -2, 5])
    assert 9 == array.sub_max()

    array = Array([-1, -2, -3, -4])
    assert -1 == array.sub_max()
