class FindAllAnagramsInAString:
    # 自己解决，看过答案后
    # 很多 String 出现的问题都用到了dictionary
    # Get fucking back to this
    def findAnagrams2(self, s, p):
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

    # Use the counter, the the point is sliding window
    def findAnagrams3(self, s, p):
        # 思路没错，但是超过了时间限制，这是为什么呢？
        # 自己更新 的优点在哪？
        from collections import Counter
        left = 0
        right = len(p)
        ans = []
        smallCount = Counter(p)
        while right <= len(s):
            winCount = Counter(s[left : right])
            if winCount == smallCount:
                ans.append(left)

            left += 1
            right += 1
        return ans

    def findAnagrams(self, s, p):
        from string import ascii_lowercase
        winLen = len(p)
        smallCount = {chr: 0 for chr in ascii_lowercase}
        winCount = {chr: 0 for chr in ascii_lowercase}
        for char in p:
            smallCount[char] += 1

        left = right = 0
        ans = []

        # This loop is borrowed from the answer, it was written very cleverly.
        # 这个Loop写的很有艺术气息 其他双指针问题会给你更多这样的锻炼

        while right < len(s):
            winCount[s[right]] += 1

            if winCount == smallCount:
                ans.append(left)

            if right - left + 1 == len(p):
                winCount[s[left]] -= 1
                left += 1

            right += 1
        return ans



