class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for num in nums:
            length = 1

            if num - 1 in numbers:
                continue

            current = num + 1
            while current in numbers:
                length = length + 1
                current = current + 1
            
            if length > longest:
                longest = length

        return longest

            

                
        