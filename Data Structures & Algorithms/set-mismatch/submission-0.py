class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        distinct = set()
        repeat = -1
        for num in nums:    
            if num in distinct:
                repeat = num
            else:
                distinct.add(num)
        
        # find the missing number
        for i in range(1, len(nums)+1):
            if i not in distinct:
                return [repeat, i]

        return [-1, -1]