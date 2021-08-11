class AddBinary:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a), len(b)

        carry = 0
        ans = ""
        # isn't it a pre-req to pinpoint two pointers for two-pointers prob

        while i > 0 or j > 0 or carry != 0:
            val1 = a[i - 1] if i - 1 > -1 else 0
            val2 = b[j - 1] if j - 1 > -1 else 0
            i, j = i - 1, j - 1
            sum = int(val1) + int(val2) + carry
            carry = sum // 2
            val = sum % 2
            ans += str(val)

        return ans[::-1]





        return 0