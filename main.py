from MergeSort1 import MergeSort1
from QuickSort import QuickSort
from QuickSort2 import QuickSort2
import random
if __name__ == '__main__':


    nums = []
    qs = QuickSort2()
    for _ in range(10):
        nums.append(random.randint(0, 100))

    print(nums)
    qs.sort(nums)
    print(nums)


    print("This is the end, hold your breath and count to ten")
