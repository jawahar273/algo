from typing import Any, List


class Array:
    def __init__(self, elements: List[Any]): 

        self._array = elements

    def size(self):
        return len(self._array)

    def is_empty(self):
        return True if len(self._array) > 0 else False

    def at(self, index: int) -> Any:
        return self._array[index]

    def push(self, element: Any) -> None:
        self._array.append(element)

    def insert(self, index: int, element: Any) -> bool:
        if self.is_empty() and index < self.size():
            self._array.insert(index, element)
            return True
        else:
            return False

    def display(self):
        print(self._array)
    
    def delete(self, index: int):
        del self._array[index]
    
    def find(self, element: Any):
        return self._array.index(element)

    def pop(self):
        return self._array.pop()

if __name__ == '__main__':
    test_array = Array([3, 4, 5, 6, 7, 8])
    test_array.display()
    test_array.insert(0, 121) 
    test_array.display()
    print(test_array.at(0))
    print('index: ', test_array.find(3))
    test_array.pop()
    test_array.pop()
    test_array.display()
