from ListNode import ListNode


class AddTwoNumbers:
    # 默写模版
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            carry = sum // 10
            val = sum % 10
            curr.next = ListNode(val)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

    # string Version
    def addTwoNumbers2(self, str1, str2):
        ans = ""
        carry = 0
        i, j = len(str1) - 1, len(str2) - 1
        while i > 0 or j > 0 or carry != 0:
            val1 = str1[i] if i >= 0 else 0
            val2 = str2[j] if j >= 0 else 0

            sum = int(val1) + int(val2) + carry
            val = sum % 10
            carry = sum // 10

            if i >= 0:
                i -= 1
            if j >= 0:
                j -= 1
            ans += str(val)

        return ans[::-1]
