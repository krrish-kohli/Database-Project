import algorithms as algo
from ArrayList import ArrayList
from DLList import DLList
import random
import copy

def test():
        """write your own tester in this function"""
        n = random.randint(8, 15)
        elements = [random.randint(-10, 10) for i in range(n)]
        arr = ArrayList(copy.deepcopy(elements))
        print("Testing Linear Search....")
        x = arr[random.randint(0, len(arr)-1)]
        idx1 = algo.linear_search(arr, x)
        expected1 = arr[idx1]
        print(f"\tArrayList: {arr}\n\tLinear Search for {x}: {idx1}\n\tPassed? {x == expected1}\n")

        dll = DLList(copy.deepcopy(elements))
        idx2 = algo.linear_search(dll, x)
        expected2 = dll[idx2]
        print(f"\tDLList: {dll}\n\tLinear Search for {x}: {idx2}\n\tPassed? {x == expected2}")

        print("\n" + '-'*50 )
        print("Testing Binary Search....")
        n = random.randint(8, 15)
        sorted_elements = sorted([random.randint(-10, 10) for i in range(n)])

        arr = ArrayList(copy.deepcopy(sorted_elements))
        x = arr[random.randint(0, len(arr) - 1)]
        idx1 = algo.binary_search(arr, x)
        expected1 = arr[idx1]
        print(f"\tArrayList: {arr}\n\tBinary Search for {x}: {idx1}\n\tPassed? {x == expected1}\n")

        dll = DLList(copy.deepcopy(sorted_elements))
        idx2 = algo.binary_search(dll, x)
        expected2 = dll[idx2]
        print(f"\tDLList: {dll}\n\tBinary Search for {x}: {idx2}\n\tPassed? {x == expected2}")

        print("\n" + '-' * 50)
        print("\nTesting Merge-Sort")

        n = random.randint(8, 15)
        elements = [random.randint(-10, 10) for i in range(n)]
        sorted_elements = sorted(copy.deepcopy(elements))
        arr = ArrayList(copy.deepcopy(elements))
        print(f"\tArrayList BEFORE sort:", arr)
        algo.merge_sort(arr)
        print("\tArrayList AFTER sort:", arr)
        print("\tExpected:", sorted_elements)

        dll = DLList(copy.deepcopy(elements))
        print(f"\n\tDLList BEFORE sort:", dll)
        algo.merge_sort(dll)
        print(f"\tDLList AFTER sort:", dll)
        print("\tExpected:", sorted_elements)


        print("\n" + '-' * 50)
        print("\nTesting Quick-Sort with Random-Element Pivot")

        n = random.randint(8, 15)
        elements = [random.randint(-10, 10) for i in range(n)]
        sorted_elements = sorted(copy.deepcopy(elements))
        arr = ArrayList(copy.deepcopy(elements))
        print(f"\tArrayList BEFORE sort:", arr)
        algo.quick_sort(arr)
        print("\tArrayList AFTER sort:", arr)
        print("\tExpected:", sorted_elements)

        n = random.randint(8, 15)
        elements = [random.randint(-10, 10) for i in range(n)]
        sorted_elements = sorted(copy.deepcopy(elements))
        dll = DLList(copy.deepcopy(elements))
        print(f"\n\tDLList BEFORE sort:", dll)
        algo.quick_sort(dll)
        print(f"\tDLList AFTER sort:", dll)
        print("\tExpected:", sorted_elements)

        print("\n" + '-' * 50)
        print("\nTesting Quick-Sort with First-Element Pivot")

        n = random.randint(8, 15)
        elements = [random.randint(-10, 10) for i in range(n)]
        sorted_elements = sorted(copy.deepcopy(elements))
        arr = ArrayList(copy.deepcopy(elements))
        print(f"\tArrayList BEFORE sort:", arr)
        algo.quick_sort(arr, False)
        print("\tArrayList AFTER sort:", arr)
        print("\tExpected:", sorted_elements)

        n = random.randint(8, 15)
        elements = [random.randint(-10, 10) for i in range(n)]
        sorted_elements = sorted(copy.deepcopy(elements))
        dll = DLList(copy.deepcopy(elements))
        print(f"\n\tDLList BEFORE sort:", dll)
        algo.quick_sort(dll, False)
        print(f"\tDLList AFTER sort:", dll)
        print("\tExpected:", sorted_elements)
