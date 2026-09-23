# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        place = 0
        curr1, curr2 = l1, l2
        carry = 0
        start = ListNode()
        current = start

        while curr1 and curr2:
            current.next = ListNode((curr1.val + curr2.val + carry) % 10)
            carry = (curr1.val + curr2.val + carry) // 10
            current = current.next
            curr1, curr2 = curr1.next, curr2.next
        
        while curr1:
            current.next = ListNode((curr1.val + carry) % 10)
            carry = (curr1.val + carry) // 10
            curr1, current = curr1.next, current.next

        while curr2:
            current.next = ListNode((curr2.val + carry) % 10)
            carry = (curr2.val + carry) // 10
            curr2, current = curr2.next, current.next

        if carry > 0:
           current.next = ListNode(carry)

        return start.next