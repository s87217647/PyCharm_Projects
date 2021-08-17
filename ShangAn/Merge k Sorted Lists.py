import ListNode
from typing import List
from heapq import heappop, heappush
ListNode.__lt__ = lambda x, y: (x.val < y.val) # Copied form YuRu
# lambda 笔记


class MergeKSortedList:
    # 自己写，而且过了，yes Mofo
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        hq = []
        cur = head = ListNode()
        for l in lists:
            if l:
                heappush(hq, l)

        while hq:
            popedNode = heappop(hq)
            cur.next = popedNode
            cur = cur.next
            if popedNode.next:
                heappush(hq, popedNode.next)

        return head.next