class FindAllAnagramsInAString:
    # 自己解决，看过答案后
    # 很多 String 出现的问题都用到了dictionary
    # Get fucking back to this
    def findAnagrams(self, s, p):

        if not s or len(p) > len(s):
            return None

        ans = []
        left = 0
        windowLen = len(p)
        right = left + windowLen
        count = {}

        # 这个2 ptrs 的 模板， [] 的 inclusive， exclusive 要想清楚
        while right < len(s):
            tempStr = s[left : right]
            temp = {}
            for char in tempStr:
                if char not in count:
                    temp[char] = 1
                else:
                    temp[char] += 1

            if count == temp:
                ans.append(left)
            left += 1
            right += 1
        return ans