class FindAllAnagramsInAString:
    # 自己解决，看过答案后
    # 很多 String 出现的问题都用到了dictionary
    # Get fucking back to this
    def findAnagrams(self, s, p):
        windowLen = len(p)
        left = 0
        right = left + windowLen
        ans = []
        count = {}
        for char in p:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

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
            right = left + windowLen
        return ans