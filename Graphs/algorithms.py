import random
from Interfaces import List


def linear_search(a: List, x: object):
    """
    uses the linear search algorithm to return the index of the given
    element if it is found in the given list; otherwise returns None.
    :param a: List subclass type; an object from a class that implements the List interface
    :param x: object type; the object to search for
    """
    pass # FIXME: Implement this method


def binary_search(a: List, x : object):
    """
    uses the binary search algorithm to return the index of the given
    element if it is found in the given SORTED list; otherwise returns None.
    :param a: List subclass type; an object from a class that implements the List interface
    :param x: object type; the object to search for
    """
    pass # FIXME: Implement this method


def _merge(a0: List, a1: List, a: List):
    """
    helper function to merge_sort(); merges list a0 and a1 into
    sorted list a
    """
    pass # FIXME: Implement this method


def merge_sort(a: List):
    """
    sorts the given list using the merge sort algorithm
    :param a: List subclass type; an object from a class that implements the List interface
    """
    pass # FIXME: Implement this method


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
    pass # FIXME: Implement this method


def _partition_r(a : List, start, end):
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
    pass # FIXME: Implement this method


def _quick_sort_f(a: List, start, end):
    """
    helper method to quick_sort(); uses quick-sort with first-element pivot
    to sort a sublist of the given list. 
    :param a: List subclass type; an object from a class that implements the List interface
    :param start: int type; the index of the first element in the sublist
    :param end: int type; the index of the last element in the sublist
    """
    pass # FIXME: Implement this method


def _quick_sort_r(a: List, start, end):
    """
    helper method to quick_sort(); uses quick-sort with random-element pivot
    to sort a sublist of the given list. 
    :param a: List subclass type; an object from a class that implements the List interface
    :param start: int type; the index of the first element in the sublist
    :param end: int type; the index of the last element in the sublist
    """
    pass # FIXME: Implement this method


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


