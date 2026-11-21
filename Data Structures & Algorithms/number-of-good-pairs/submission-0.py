class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        counts = {}
        for num in nums:
            if num in counts:
                result += counts[num]
            counts[num] = counts.get(num, 0) + 1
        return result