class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if len(nums) <= 1:
            return True
        
        increasing, decreasing = True, True
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > prev:
                decreasing = False
            elif nums[i] < prev:
                increasing = False
            if increasing == False and decreasing == False:
                return False   
            prev = nums[i]
        return True
