class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2 9 8 3 6
        # start at 2: 2 9 10 12 16  
        # start at 9: 9 9 12 15 15

        # 2 9 10 12
        # 9 9 12 15

        if len(nums) == 1:
            return nums[0]

        i, j = 0, 1
        rob1, rob2 = 0, 0
        rob1_2, rob2_2 = 0,0
        while i < len(nums)-1:
            first_rob = max(rob1 + nums[i], rob2)
            second_rob = max(rob1_2 + nums[j], rob2_2)
            rob1 = rob2
            rob2 = first_rob
            rob1_2 = rob2_2
            rob2_2 = second_rob
            i += 1
            j += 1  
            
        return max(rob2, rob2_2)
