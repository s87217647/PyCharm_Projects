# 4.  Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution , and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Constraints:
#
# 2 <= nums.length <= 103
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

#  这道题是送分题，题之外的表现就更重要，clearificaiton, 多办法解决。
#  时间，空间复杂度，brute，Hash table, 2 pointers
# 排序，会影响 解题方法

from typing import List

# Sort array, 2 pointers
class TwoSum:
    def two_sum(self, nums: List[int], target):
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]

        return None

    # Fuck your motherfuckering brute force

