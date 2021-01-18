# Topics: Minimum number of jumps

from typing import List, Any


class Array:

    def __init__(self, elements: List[Any], n: int = 0) -> None:
        self.elements = elements
        self.n = len(elements)

    def minimum_jump(self) -> int:
        if self.n == 0 and self.n == 1:
            return self.n
        
        jump_count = 1 
        jump_element = self.elements[0]
        print("elements", self.elements)
        for inx in range(1, self.n):
            print("inx:", inx, " jump_element:", jump_element, " jump + inx:", jump_element + inx, jump_element + inx >= self.n)
            if jump_element + inx >= self.n:
                print("break")
                break
            jump_count += 1
            jump_element = self.elements[jump_element]

        return jump_count

# Need more working
array = Array(elements=[1, 4, 3, 2, 6, 7], n=6) # ans: 
array = Array(elements=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], n=11) # ans: 3
array = Array(elements=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], n=10) # ans: 10
array = Array(elements=[2, 3, 1, 1, 4], n=5) # ans: 2




print(array.minimum_jump())
