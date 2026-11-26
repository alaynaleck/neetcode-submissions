# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

""""
   1
 2   3
4 5 6 7

4 = 0
5 = 0
2 = 2
6 = 0
7 = 0
3 = 2

"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        largestDiameter = 0
        def getDiameter(root):
            nonlocal largestDiameter
            if not root:
                return 0
            left = getDiameter(root.left)
            right = getDiameter(root.right)
            largestDiameter = max(largestDiameter, left + right)
            return 1 + max(left, right)
        
        getDiameter(root)
        return largestDiameter
        
        