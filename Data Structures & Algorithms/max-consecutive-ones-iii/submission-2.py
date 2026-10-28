class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flips = 0
        left = longest = 0
        for right in range(len(nums)):
            flips += 1 if nums[right] == 0 else 0
            while flips > k:
                flips -= 1 if nums[left] == 0 else 0
                left += 1
            longest = max(longest, right - left + 1)
        return longest
                