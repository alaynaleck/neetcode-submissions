class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def binSearch(target):
            left, right = 0, n
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
    
        leftBound = binSearch(target)
        if leftBound == len(nums) or nums[leftBound] != target :
            return [-1, -1]
        
        rightBound = binSearch(target + 1) - 1
        return [leftBound, rightBound]


    