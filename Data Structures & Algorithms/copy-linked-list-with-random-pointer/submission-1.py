"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        current = head
        copies = { None : None } # key: original Node, val: copy Node

        def getCopy(node: Node) -> 'Optional[Node]':
            if node not in copies:
                copies[node] = Node(0)
            return copies[node]

        copies[head] = getCopy(head)
        while current:
            copies[current].val = current.val
            copies[current].next = getCopy(current.next)
            copies[current].random = getCopy(current.random)
            current = current.next
        
        return copies[head]



