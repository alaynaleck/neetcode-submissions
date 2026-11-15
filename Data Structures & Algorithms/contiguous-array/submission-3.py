class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeroes, ones, maxLength = 0, 0, 0
        diffs = {} # key: difference of ones and zeros, val: index ending at
        for currentIndex, num in enumerate(nums):
            if num == 1:
                ones += 1
            elif num == 0:
                zeroes += 1
            if ones - zeroes not in diffs:
                diffs[ones - zeroes] = currentIndex
            if ones == zeroes:
                maxLength = ones + zeroes
            else:
                start = diffs[ones - zeroes]
                maxLength = max(maxLength, currentIndex - start)
        return maxLength
