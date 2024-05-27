from SLLQueue import SLLQueue
from SLLStack import SLLStack
from DLList import DLList
from DLLDeque import DLLDeque
from MaxQueue import MaxQueue
import random

def test():
    """write your own tester in this function"""
    print("Testing MaxQueue...")
    mq = MaxQueue()
    import random

    for i in range(6):
        value = random.randint(1, 20)
        mq.add(value)
        print("Added value:", value)
        print(f"Max Queue: {mq}")
        print(f"Max value: {mq.max()}\n")

    while mq.size() > 0:
        r = mq.remove()
        print(f"Removed:", r)
        print(f"MaxQueue:", mq)
        if mq.size() > 0:
            print(f"Max value: {mq.max()}\n")