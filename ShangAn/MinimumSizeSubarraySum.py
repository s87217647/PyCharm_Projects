from typing import List
class MinimumSizeSubarraySum:
    # Nums 出现负数会影响结果
    # 记得 Clarify
    # 这两个Loop 作为模板
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans, sum = len(nums) + 1, 0
        left = right = 0
        while right < len(nums):
            sum += nums[right]
            while sum >= s:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1

            right += 1

        return ans if ans != len(nums) + 1 else 0