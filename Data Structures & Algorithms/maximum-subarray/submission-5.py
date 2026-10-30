class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result, total = nums[0], 0
        for num in nums:
            if total < 0: 
                total = 0
            total += num
            result = max(total, result)
        return result
            