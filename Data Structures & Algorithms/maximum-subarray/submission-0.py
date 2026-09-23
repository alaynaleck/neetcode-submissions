class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Sliding window? 
        # we could brute force and check every permutation
        # we found find the average - that number?
        max_sum, current_sum = nums[0], 0
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum
