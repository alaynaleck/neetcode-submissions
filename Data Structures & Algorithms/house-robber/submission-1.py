class Solution:
    def rob(self, nums: List[int]) -> int:
        # is it cheaper to rob the houses before or the current house
        # first and second  house always have the same amounts
        # ex. first house: no other options , 2
        # second: 9 or 2, 9 is greater
        # third: 10 (cur + rob(i-2)) or 9 (rob i-1) 10 is greater
        # fourth: 12 (rob i - 1) or 10, 12 is greater 
        # fifth: 16 or 12 
        # 2, 9, 10, 12, 16
        # 2 1 1 2
        # first: 2
        # second 2 (current = 1, prior = 2, take 2)
        # third, ()

        two_before = 0
        one_before = 0
        max_money = 0
        for num in nums:
            current = two_before + num
            max_money = max(current, one_before)

            # Update the previous
            two_before = one_before
            one_before = max_money
            
        return max_money
