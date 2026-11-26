# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):

            if not root:
                return 0
            
            leftHeight = dfs(root.left)

            # Left height is inbalanced
            if leftHeight == -1:
                return -1 

            rightHeight = dfs(root.right)

            # Right height is inbalanced or the tree is now imbalanced
            if rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            
            # Return the height
            return 1 + max(leftHeight, rightHeight)

        return False if dfs(root) == -1 else True
