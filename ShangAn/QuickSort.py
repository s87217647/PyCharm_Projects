class QuickSort:
    #老夫子的3 Way partition
    # You will have to just remember it bro.
    # The holy grail
    def sort(self, nums):
        self.qs(nums, 0, len(nums) - 1)

    def qs(self, nums, lo, hi):
        if lo >= hi:
            return

        mid = self.partition(nums, lo, hi)
        self.qs(nums, lo, mid - 1)
        self.qs(nums, mid + 1, hi)

    def partition(self, nums, lo, hi):
        pivot = nums[lo]
        while lo < hi:
            while lo < hi and nums[hi] >= pivot:
                hi -= 1
            nums[lo] = nums[hi]

            while lo < hi and nums[lo] <= pivot:
                lo += 1
            nums[hi] = nums[lo]

        nums[lo] = pivot
        return lo
