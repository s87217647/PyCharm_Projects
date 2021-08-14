class MinimumWindowSubstring:
    def minWindow(self, s, t):
        # 尝试自己解题
        if len(t) > len(s):
            return ""
        ans = []
        for char in t:
            strPtr = 0
            while s[strPtr] != char:
                strPtr += 0
                ans.append(strPtr)

        first = min(ans)
        last = max(ans)

        return s[first:last]