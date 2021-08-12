from ListNode import ListNode

class AddTwoNumbersII:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        carry = 0
        cur = dummy
        while l1 or l2 or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            carry = sum // 10
            val = sum % 10
            cur.next = ListNode(val)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            return dummy.next

    # I want to cheat this fucker: the idea is simple, recursive get both numbers
    # add two fuckers up. Boom shakalaka
    def addTwoNumbersII2(self, l1: ListNode, l2:ListNode):
        int1 = self.findInt(l1)
        int2 = self.findInt(l2)
        intStr = str(int1 + int2)
        print(intStr)

        head = ListNode()
        cur = head
        for char in intStr:
            cur.next = ListNode(int(char))
            cur = cur.next

        return head.next


    def findInt(self, head: ListNode) -> int:
        intStr = ""
        while head:
            intStr += str(head.val)
            head = head.next

        return int(intStr)


