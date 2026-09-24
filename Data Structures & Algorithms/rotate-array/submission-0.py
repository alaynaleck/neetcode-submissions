class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seen = 0
        start, prev = 0, 0
        current, prev = start, nums[start]

        while seen < len(nums):
            current, prev = start, nums[start]
            while True:
                rotate = (current + k) % len(nums)
                nums[rotate], prev = prev, nums[rotate]
                current = rotate
                seen += 1
                if start == current:
                    break
            start += 1
        return 
        