class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def createSubset(subset, appendIndex):
            if appendIndex == len(nums):
                result.append(list(subset))
                return

            # Skip the element
            createSubset(subset, appendIndex + 1)

            # Try the next element and backtrack to restore without the try
            subset.append(nums[appendIndex])
            createSubset(subset, appendIndex + 1)
            subset.pop()

        createSubset([], 0)
        return result