class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] # List of all permutations
    
        def createPermutation(nums, swapIndex):
            # All elements have been swapped, meaning a unique combo = reached
            if swapIndex == len(nums):
                result.append(list(nums))

            # For each unswapped element in the array, try a new permutation 
            # With swap inserted at a different position
            for i in range(swapIndex, len(nums)):

                # Swap the current position and the swap position to create a new perm
                nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
                createPermutation(nums, swapIndex + 1)

                # Swap them back to restore the original array
                nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
        
        createPermutation(nums, 0)
        return result