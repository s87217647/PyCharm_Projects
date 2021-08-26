from typing import Set

class LongestSubstringwithAtMostKDistinctCharacters:
    # clarify: sorted? What if no ans

    def lengthOfLongestSubstringKDistinct(self, s: str) -> int:
        ans = 0
        # how do I know if it's distinct or not?
        # set? dict?
        # lemme try using set aye?
        left = right = ans = 0
        count = {}

        while left < len(s):
            while right < len(s):
                count = count.get(s[right], 0) + 1
                right += 1
                if count[s[right]] <= 2:
                    ans = max(ans, right - left)
                else:
                    break
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

        return ans