class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1} # remainder, index it was seen at
        total = 0
        for i, num in enumerate(nums):
            total = (total + num) % k
            if total not in remainders:
                remainders[total] = i
            elif i - remainders[total] > 1:
                return True
        return False