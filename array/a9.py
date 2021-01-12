# Topic: Minimise the maximum difference between heights 

from typing import List, Any


class Array:
    def __init__(self, elements: List[Any]) -> None:
        self.elements = elements
    
    def get_min_diff(self, n: int, k: int) -> int:
        self.elements.sort()
        ans   = self.elements[n-1] - self.elements[0]
        small = self.elements[0] + k
        big   = self.elements[n-1] - k
        if small > big:
            small, big = big, small

        for element in self.elements[1:]:
            add_k = element + k
            sub_k = element - k

            if (sub_k >= small or add_k >= big):
                continue
            if (big - small <= add_k - sub_k):
                small = sub_k
            else:
                big   = add_k

        return min((ans, big - small))

array = Array([1, 5, 8, 10])

print("Minimize the heights: ", array.get_min_diff(
    len(array.elements), 2
))


def test_a9():
    array = Array([3, 9, 12, 16, 20])
    assert array.get_min_diff(5, 3) == 11

