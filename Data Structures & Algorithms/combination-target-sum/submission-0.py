class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def createCombination(combination, index, currentSum):
            if currentSum == target:
                result.append(combination.copy())

            for i in range(index, len(nums)):
                if currentSum + nums[i] > target:
                    return
                combination.append(nums[i])
                createCombination(combination, i, currentSum + nums[i])
                combination.pop()
      
        createCombination([], 0, 0)      
        return result
