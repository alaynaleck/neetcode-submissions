# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Understand: 
An inverted binary tree is one in which its nodes, left and right, are reversed
Inputs: 
- Root with two children: switch its children
- Null: return none
- One node: return only that node
- Node with only one node: switch even though its null
- Non-binary tree values? do we handle these? 

Match: 
Binary Tree, pre-order traversal, can be recursive
This is pre-order because you can switch each level then move to the next

Plan: 
- Check if the root null ? root : continue
- Check if the root has no children ? root : continue
- Create a temp node of left
- root.left = root.right, root.right = temp
- travese to the right and traverse to the left



'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    

        
        