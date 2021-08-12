class AddToArrayForm:
    def addToArrayForm(self, num, k):
        intStr = str(k)

        carry = 0
        ans = []
        i, j = len(num) - 1, len(intStr) - 1

        while i >= 0 or j >= 0 or carry != 0:
            val1 = num[i] if i >= 0 else 0
            val2 = intStr[j] if j >= 0 else 0
            val2 = int(val2)
            sum = val1 + val2 + carry
            val = sum % 10
            carry = sum // 10
            ans.append(val)
            i -= 1
            j -= 1

        return ans[::-1]