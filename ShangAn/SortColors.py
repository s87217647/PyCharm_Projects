class SortColors:
    #This is straight up quick sort test
    # Buck sort
    # Is  this a three pointers question?
    #抄写
    def sortColors(self, nums):

        left, right, i = 0, len(nums) - 1, 0
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left, i = left + 1, i + 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1

