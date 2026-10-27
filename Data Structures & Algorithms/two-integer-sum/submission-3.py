class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store a hashmap of val, index
        indices = {}
        for j, num in enumerate(nums):
            partner = target - num
            if partner in indices:
                return [indices[partner], j]
            indices[num] = j
        return [-1, -1]