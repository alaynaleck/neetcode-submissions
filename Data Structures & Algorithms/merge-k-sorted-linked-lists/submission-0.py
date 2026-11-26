# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node == None:
                continue
            heapq.heappush(heap, (node.val, i, node))

        current = temp = ListNode(0)
        while heap:
            val, i, nxt = heapq.heappop(heap)
            current.next = nxt
            if nxt.next:
                heapq.heappush(heap, (nxt.next.val, i, nxt.next))
            current = current.next
        return temp.next
