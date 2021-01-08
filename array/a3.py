from typing import List, Any

def kthSmallElement(arr: List[Any], k: int):
    '''
        arr: process array 
        k: kth element index(kth index must start with 1)
    '''
    assert k <= len(arr) and k > 0
    return sorted(arr)[k-1]


print('Displaying kth small element:', kthSmallElement([7, 10, 4, 3, 20, 15], 1))


def test_a3():
    assert kthSmallElement([7, 10, 4, 3, 20, 15], 3) == 7
    assert kthSmallElement([7, 10, 4, 20, 15], 4) == 15
