class LongestSubstringWithoutRepeatingCharacters:
    #自己解
    #答案应该是正确的，时间太长了
    def lengthOfLongestSubstring(self, s):
        left, right = 0, 0
        minLen = float('inf')
        while left < len(s) - 1:
            right = left
            while s[right] not in s[left:right]:
                right += 1

            minLen = min(minLen, left - right)
            left + 1

        return minLen

    #上岸
    def lengthOfLongestSubstring2(self, s):
        left, right, count = 0,0,{}
        ans = 0
        while right < len(s):
            if s[right] not in count: # If and else can not be swap,
                count[s[right]] = 1    # have to crate first
            else:
                count[s[right]] += 1

            # 不满足条件的窗口就一直往左滑
            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left +1)
            right += 1

        return ans


