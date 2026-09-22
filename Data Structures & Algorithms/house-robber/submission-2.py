class Solution:
    def rob(self, nums: List[int]) -> int:
        two_before = 0
        one_before = 0
        max_money = 0

        for num in nums:
            max_money = max(two_before + num, one_before)

            # Update the previous
            two_before = one_before
            one_before = max_money
            
        return max_money
