#This file is simply 默写
#Todo: Compare merge sort with quick sort

class QuickSort2:
    def sort(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return

    def quickSort(self, nums, start, end):
        if start >= end:
            return
        mid = self.partition(nums, start, end)
        self.quickSort(nums, start, mid - 1)
        self.quickSort(nums, mid + 1, end)

    def partition(self, nums, start, end):
        i, j, pivot = start + 1 , end, nums[start] # 这个地方默写出错了，下次默写的时候重点关注, "+1", pivot 是 start + 1
        while i <= j:
            while i <= j and nums[i] <= pivot:
                i += 1
            while i <= j and pivot < nums[j]:
                j -= 1

            if i > j:
                break

            self.swap(nums, i, j)
            i += 1
            j -= 1

        nums[start] = nums[j]
        nums[j] = pivot



        return j



    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

