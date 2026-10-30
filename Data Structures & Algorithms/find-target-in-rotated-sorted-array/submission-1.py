class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right-left)//2 + left
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        shifts = left - 1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right-left)//2 + left
            shiftedMid = (mid + shifts) % len(nums)
            if nums[shiftedMid] == target:
                return shiftedMid
            elif nums[shiftedMid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
    
