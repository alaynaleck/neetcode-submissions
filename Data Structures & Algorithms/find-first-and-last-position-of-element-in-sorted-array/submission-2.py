class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def binSearch(left, right, target):
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
    
        leftBound = binSearch(0, n, target)
        if leftBound == len(nums) or nums[leftBound] != target :
            return [-1, -1]
        
        rightBound = binSearch(leftBound, n, target + 1) - 1
        return [leftBound, rightBound]


    