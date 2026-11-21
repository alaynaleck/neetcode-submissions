class Solution:
    def check(self, nums: List[int]) -> bool:
        rotated = False
        for i in range(len(nums) - 1):

            # Ignore numbers that are correctly ordered
            if nums[i] <= nums[i+1]:
                continue

            # Incorrectly ordered numbers are invalid 
            # if the array has already been rotated
            if rotated:
                return False
            rotated = True
    
        return False if nums[0] < nums[-1] and rotated else True
            
        
                