# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        
        # Traverse the list until we stop at the left
        dummy = ListNode(0, head)
        leftPrev, current = dummy, head
        while current and index < left:
            leftPrev, current = current, current.next
            index += 1
        
        prev = None
        # Reverse nodes until we reach the right
        while current and index <= right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            index += 1

        leftPrev.next.next = current
        leftPrev.next = prev
        return dummy.next




        
