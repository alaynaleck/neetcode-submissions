class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binSearch(target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2 
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        start = binSearch(target)
        # Target is not found
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        # Search greater than the target (will end right before)
        return [start, binSearch(target+1)-1]