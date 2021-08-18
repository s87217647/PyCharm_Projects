from typing import List
from heapq import heappush, heappop


class KthLargest:
    # 2 solution
    # quickSelect # require you to revisit quicksort first
    # minheap
    # 找到老夫子老师推荐的QuickSort 再背一遍

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return None

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        #这个method 可以被优化，可以根据 K 和 len 的关系，选择使用Max heap or  min heap
        minHeap = []
        for num in nums:
            heappush(minHeap, num)
            if len(minHeap) > k:
                heappop(minHeap)

        return heappop(minHeap)
