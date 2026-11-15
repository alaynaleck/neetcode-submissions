# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rightMost = []
        queue = deque([(root, 0)])
        while queue:
            current, level = queue.popleft()
            if not current:
                continue

            if level >= len(rightMost):
                rightMost.append(current.val)
            else: 
                rightMost[level] = current.val 

            queue.append((current.left, level + 1))
            queue.append((current.right, level + 1))

        return rightMost