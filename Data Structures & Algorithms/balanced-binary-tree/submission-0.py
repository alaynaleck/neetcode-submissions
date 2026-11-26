# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Understand:
        Return if the binary tree is balanced: left and right subtrees of all nodes differ by no  more than one
        Match: Post order traversal, we want to check the bottom subtrees
        Plan:
        - At a given instance we want to know the height or a given subtree, or if it differs by more than one
        we could do this iteratively
        """
        def dfs(root):

            if not root:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            
            return 1 + max(leftHeight, rightHeight)

        return False if dfs(root) == -1 else True
