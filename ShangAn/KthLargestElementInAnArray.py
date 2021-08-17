from typing import List
from typing import Set
class KthLargestElementInAnArray:

    #还可以应用Quick Select
    #Let's reveiw the fucking quick sort, then do the quick select.
    # 这虽然正确，但肯定不是要要考的点
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        min_heap = []
        import heapq
        for num in nums:
            heapq.heappush(min_heap, num)
            # TODD: find queue, duplicated
            # How the data inside is arranged?
            if len(min_heap) > k: # how about repeated ones?
                heapq.heappop(min_heap)
        return min_heap[0]

        # And this method did not fucking pass
    # partial partition
    # min heap