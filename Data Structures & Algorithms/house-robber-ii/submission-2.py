class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def try_rob(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                current_rob = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = current_rob
            return rob2

        return max(try_rob(nums[:-1]), try_rob(nums[1:]))
