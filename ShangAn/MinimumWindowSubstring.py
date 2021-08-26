class MinimumWindowSubstring:
    def minWindow(self, s, t):
        # 尝试自己解题
        # Min Win 的 模板是没错，要怎么判断一个东西是另一个东西的Sub Str？
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