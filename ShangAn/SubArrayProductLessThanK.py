from typing import List


class SubarrayProductLessThanK:
    def SubarrayProductLessThanK(self, nums, k):
        #Subarray is continous, so it's likely to be two pointers

        #Clarification:
        # nums, None? Sorted?
        # ans duplicates? Two section are the same?
        ans = 0
        left = 0

        while left < len(nums):
            product = 1
            right = left
            innerAns = [[]]
            while right < len(nums):
                product *= nums[right]
                if product < k:
                    ans += 1

                right += 1
            left += 1

        return ans
    #答案应该是对的，但是 时间复杂度太长了

    # 这是上岸给答案
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        product, total, start_index = 1, 0, 0
        for i in range(len(nums)):
            product *= nums[i]
        # Sneaky sneaky bastard
            while product >= k and start_index < i: # 这一步真聪明，乘所有东西，从左边开始往右削
                product /= nums[start_index]
                start_index += 1
            if product < k:
                total += i - start_index + 1
        return total