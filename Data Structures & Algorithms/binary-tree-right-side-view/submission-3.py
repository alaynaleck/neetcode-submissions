# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightMost = []
        
        def dfs(node, level):
            if not node:
                return
            if level == len(rightMost):
                rightMost.append(node.val)
            
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 0)
        return rightMost