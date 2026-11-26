class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def createTree(left, right, root):
            if right < left:
                return None
            mid = left + (right - left) // 2 
            root = TreeNode(nums[mid])
            root.left = createTree(left, mid - 1, root.left)
            root.right = createTree(mid + 1, right, root.right)
            return root

        return createTree(0, len(nums) - 1, None)




