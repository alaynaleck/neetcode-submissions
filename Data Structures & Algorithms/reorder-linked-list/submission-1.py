# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Understand:
        0 -> 0
        0,1 -> 0,1
        0,1,2 -> 0,2,1
        0,1,2,3 -> 0,3,1,2
        0,1,2,3,4 -> 0,4,1,3,2

        We could use a fast and a slow pointer to detect the middle
        once we detect the middle, we add the remaining nodes to a stack
        
        start at the head of the list and create a current; while current or stack
        next = current.next
        current.next = stack.pop()
        current.next.next = current.next
        current = current.next.next
        """

        slow, fast = head, head
        # The slow will reach the middle when the fast
        # Reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        stack = []
        while slow:
            stack.append(slow)
            slow = slow.next

        current = head
        while current and current.next and stack:
            nxt = current.next
            current.next = stack.pop()
            current.next.next = nxt
            current = current.next.next
        current.next = None
            

        