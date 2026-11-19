# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Understand: Merge two sorted lists into one
        - One could be longer than the other
        - We need to find a way to keep the loop going while the other doesn't exist

        - if both exists: 
        we want l1.next = l2, then how do we get l2.next to equal l1.next? 


        """
        dummy = node = ListNode(0)
        l1 = list1
        l2 = list2
        while l1 and l2:

            if l1.val <= l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)   
                l2 = l2.next

            node = node.next

        while l1:
            node.next = ListNode(l1.val)
            l1 = l1.next
            node = node.next
        
        while l2:
            node.next = ListNode(l2.val)
            l2 = l2.next
            node = node.next
            
        return dummy.next

            
            