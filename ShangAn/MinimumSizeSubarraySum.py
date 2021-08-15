class MinimumSizeSubarraySum:
    # Nums 出现负数会影响结果
    # 记得 Clarify
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0,0
        ans = len(nums) + 1

        while right < len(nums):
            if sum (nums[left : right]) >= target:
                ans = min(ans, right - left)
                left += 1

            right += 1

        return 0 if ans > len(nums) else ans
