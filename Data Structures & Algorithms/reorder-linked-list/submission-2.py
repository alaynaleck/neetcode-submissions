# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head
        # The slow will reach the middle when the fast
        # Reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        endHalf = slow.next
        slow.next = None

        prev = None
        current = endHalf
        # Reverse the second half of the list
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        current = head
        merge = prev
        while current and merge:
            nxt = current.next
            current.next = merge
            merge = merge.next
            current.next.next = nxt
            current = current.next.next

        