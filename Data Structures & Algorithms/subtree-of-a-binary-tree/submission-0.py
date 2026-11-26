# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(root, subRoot):
            
            if not root and not subRoot:
                return True
            
            if root and subRoot and root.val == subRoot.val:
                return isEqual(root.left, subRoot.left) and isEqual(root.right, subRoot.right)
            return False


        
        def findSubtree(root):
            
            if not root:
                return False

            if isEqual(root, subRoot):
                return True
            
            return findSubtree(root.left) or findSubtree(root.right)

        return findSubtree(root)

