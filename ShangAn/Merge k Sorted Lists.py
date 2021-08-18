import ListNode
from typing import List
from heapq import heappop, heappush

# You are not familiar with the data structure, but it's OK, for this problem
# just remember heappop and push will maintain the heap with it's property
class MergekSortedLists:

    # TODO: Understand this porgram
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = point = ListNode(0)
        q = []
        for l in lists:
            if l:
                heappush(q, (l.val, id(l), l))
        while q:
            val, nodeId, node = heappop(q) # What's the purpose of this ID? It has never be used
            point.next = node
            point = point.next # point = point.next = node ?
            node = node.next
            if node:
                heappush(q, (node.val, id(node), node))
        return head.next