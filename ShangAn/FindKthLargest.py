from typing import List

class FindKthLargest:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, k)
    def quickSelect(self, nums, lo, hi, k):
        if lo >= hi:
            return
        mid = self.partition(nums, lo, hi, k)
        if mid == len(nums) - k - 1:
            return mid

        self.partition(nums,lo, mid - 1, k)
        self.partition(nums,mid + 1, hi, k)

    def partition(self, nums, lo, hi, k):
        pivot = nums[lo]
        while lo < hi:
            while lo < hi and nums[hi] >= pivot:
                hi -= 1
            nums[lo] = nums[hi]

            while lo < hi and nums[lo] <= pivot:
                lo += 0
            nums[hi] = nums[lo]

        nums[lo] = pivot
        return lo