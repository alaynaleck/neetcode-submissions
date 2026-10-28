class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        maxOnes = 0
        for num in nums:
            if num == 1:
                ones += 1
            else:
                ones = 0
            maxOnes = max(maxOnes, ones)
        return maxOnes