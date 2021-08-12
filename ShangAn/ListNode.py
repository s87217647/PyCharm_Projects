class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def arrayInput(self, arr):
        if not arr:
            return

        head = ListNode()
        cur = head
        for num in arr:
            cur.next = ListNode(num)
            cur = cur.next
        return head.next

    def display(self, cur):
        output = []
        while cur:
            output.append(cur.val)
            cur = cur.next
        print(output)