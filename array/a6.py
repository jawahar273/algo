# Topic: Find the Union and Intersection of the two sorted arrays.

from typing import Any, Set

def union_array(arr1: Set[Any], arr2: Set[Any]):
    arr1 = set(arr1)
    arr2 = set(arr2)
    return arr1.union(arr2)

print(sorted(union_array([85, 25, 1, 32, 54, 6], [85, 2])))

def test_a6():
    assert sorted(union_array([1, 2, 3, 4, 5], [1, 2, 3])) == [1, 2, 3, 4, 5]
    assert sorted(union_array([7, 1, 5, 2, 3, 6], [3, 8, 6, 20, 7])) == [1, 2, 3, 5, 6, 7, 8, 20]
