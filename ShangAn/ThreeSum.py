# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
#
# Input: nums = []
# Output: []
# Example 3:
#
# Input: nums = [0]
# Output: []
# Constraints:
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105


# 现在照着答案抄了一遍
# Hash map 也可以
from typing import List
from TwoSum import TwoSum

class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -1 * nums[i]

            left, right = i + 1, len(nums) - 1

            while left < right:
                # 大于 target 需要小一些，小于Target需要大一些
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + left[right] > target:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                return ans

    def threeSum2(self, nums, target) -> bool:
        ts = TwoSum()
        for i in range(len(nums)):
            twoSumTarget = target - nums[i]
            if ts.two_sum(nums[1:],twoSumTarget):
                return True

        return False
