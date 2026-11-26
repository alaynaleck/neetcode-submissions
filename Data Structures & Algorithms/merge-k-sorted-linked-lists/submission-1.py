# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeComparator:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, NodeComparator(node))

        current = temp = ListNode(0)

        while heap:
            comparator = heapq.heappop(heap)
            current.next = comparator.node
            
            if comparator.node.next:
                heapq.heappush(heap, NodeComparator(comparator.node.next))

            current = current.next

        return temp.next
