class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        maxLength = 0
        onesCount = 0
        for currentLength, num in enumerate(nums, 1):
            onesCount += num
            if currentLength - onesCount == onesCount:
                maxLength = max(maxLength, currentLength)
        
        onesCount = 0
        for i in range(len(nums)-1, -1, -1):
            onesCount += nums[i]
            currentLength = len(nums) - i
            if currentLength - onesCount == onesCount:
                maxLength = max(maxLength, currentLength)
        
        return maxLength