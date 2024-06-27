import random
from Interfaces import List


def linear_search(a: List, x: object):
    """
    uses the linear search algorithm to return the index of the given
    element if it is found in the given list; otherwise returns None.
    :param a: List subclass type; an object from a class that implements the List interface
    :param x: object type; the object to search for
    """
    for i in range(a.size()):
        if a.get(i) == x:
            return i
    return None


def binary_search(a: List, x : object):
    """
    uses the binary search algorithm to return the index of the given
    element if it is found in the given SORTED list; otherwise returns None.
    :param a: List subclass type; an object from a class that implements the List interface
    :param x: object type; the object to search for
    """
    left, right = 0, a.size() - 1
    while left <= right:
        mid = (left + right) // 2
        if a.get(mid) == x:
            return mid
        elif a.get(mid) < x:
            left = mid + 1
        else:
            right = mid - 1
    return None


def _merge(a0: List, a1: List, a: List):
    """
    helper function to merge_sort(); merges list a0 and a1 into
    sorted list a
    """
    i = j = 0
    while i + j < a.size():
        if j == a1.size() or (i < a0.size() and a0.get(i) < a1.get(j)):
            a.set(i + j, a0.get(i))
            i += 1
        else:
            a.set(i + j, a1.get(j))
            j += 1


def merge_sort(a: List):
    """
    sorts the given list using the merge sort algorithm
    :param a: List subclass type; an object from a class that implements the List interface
    """
    n = a.size()
    if n < 2:
        return
    mid = n // 2
    a0 = a[0:mid]
    a1 = a[mid:n]
    merge_sort(a0)
    merge_sort(a1)
    _merge(a0, a1, a)


def _partition_f(a :List, start: int, end: int):
    """
    helper function to _quick_sort_f(); partitions a sublist of the given list
    using the first element of the sublist as pivot. The elements of the sublist 
    are arranged into two groups: the first group consists of elements 
    that are less than or equal to the pivot. The second group is
    a group of elements that are greater than the pivot.  By the end of the 
    partitioning process, the pivot is placed in its correct, sorted order,
    elements in the first group appear to the left of the sorted pivot, and 
    elements in the second group appear to the right of the sorted pivot.
    :param a: List subclass type; an object from a class that implements the List interface
    :param start: int type; the index of the first element in the sublist that will be partitioned
    :param end: int type; the index of the last element in the sublist that will be partitioned
    :return: int type; the final index of the pivot element
    """
    left = start + 1
    right = end
    pivot = a[start]
    crossed = False
    while not crossed:
        while left <= right and a[left] <= pivot:
            left +=1
        while a[right] >= pivot and right >= left:
            right -= 1
        if left < right:
            a[left], a[right] = a[right], a[left]
        else:
            crossed = True
    a[start], a[right] = a[right], a[start]
    return right



def _partition_r(a : List, start: int, end: int):
    """
    helper method to _quick_sort_r(); partitions a sublist of the given list
    using a random element in the sublist as pivot. The elements of the sublist
    are arranged into two groups: the first group consists of elements 
    that are less than or equal to the pivot. The second group is
    a group of elements that are greater than the pivot.  By the end of the 
    partitioning process, the pivot is placed in its correct, sorted order,
    elements in the first group appear to the left of the sorted pivot, and 
    elements in the second group appear to the right of the sorted pivot.
    :param a: List subclass type; an object from a class that implements the List interface
    :param start: int type; the index of the first element in the sublist that will be partitioned
    :param end: int type; the index of the last element in the sublist that will be partitioned
    :return: int type; the final index of the pivot element
    """
    pivot = random.randint(start, end)
    a[start], a[pivot] = a[pivot], a[start]
    return _partition_f(a, start, end)


def _quick_sort_f(a: List, start: int, end: int):
    """
    helper method to quick_sort(); uses quick-sort with first-element pivot
    to sort a sublist of the given list. 
    :param a: List subclass type; an object from a class that

 implements the List interface
    :param start: int type; the index of the first element in the sublist
    :param end: int type; the index of the last element in the sublist
    """
    if start < end:
        split = _partition_f(a, start, end)
        _quick_sort_f(a, start, split - 1)
        _quick_sort_f(a, split + 1, end)


def _quick_sort_r(a: List, start, end):
    """
    helper method to quick_sort(); uses quick-sort with random-element pivot
    to sort a sublist of the given list. 
    :param a: List subclass type; an object from a class that implements the List interface
    :param start: int type; the index of the first element in the sublist
    :param end: int type; the index of the last element in the sublist
    """
    if start < end:
        split = _partition_r(a, start, end)
        _quick_sort_r(a, start, split - 1)
        _quick_sort_r(a, split + 1, end)


def quick_sort(a: List, p=True):
    """
    sorts the given List using the quick sort algorithm.
    :param a: List subclass type; an object from a class that 
    implements the List interface
    :param p: boolean type; if True, the quick-sort algorithm uses a
              randomly chosen element from a as pivot. 
              Otherwise, uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size() - 1)
    else:
        _quick_sort_f(a, 0, a.size() - 1)