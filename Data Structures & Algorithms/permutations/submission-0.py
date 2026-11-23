class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] # List of all permutations
        selected = [0 for i in range(len(nums))] # i = i of nums, val = seen/unseen

        def createPermutation(arr, selected):
            # Base case: we've used all unique nums already
            if len(arr) == len(nums):
                result.append(list(arr))
                return

            # Recursive: add the next unselected to the permutation
            for i in range(len(nums)):

                # Only use numbers from outside our current permutation
                if selected[i] == 0:
                    arr.append(nums[i])
                    selected[i] = 1
                    createPermutation(arr, selected)

                    # Backtrack the choice once to try 
                    # a diff number for the same position
                    arr.pop()
                    selected[i] = 0
                
        createPermutation([], selected)
        return result