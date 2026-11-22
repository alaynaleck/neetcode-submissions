# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Count the number of nodes in the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Remove index
        remove = length - n
        index = 0
        dummy = ListNode(-1,head)
        current = dummy
        while current and current.next:
            if index == remove:
                current.next = current.next.next
            index += 1
            current = current.next
        return dummy.next
            