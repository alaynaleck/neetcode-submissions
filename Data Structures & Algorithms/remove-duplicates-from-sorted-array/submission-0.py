class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        prev = None
        for read in nums:
            if read == prev:
                continue
            nums[write] = read
            prev = read
            write += 1
        return write