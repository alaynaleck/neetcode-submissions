class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        arrayLength = len(nums)
        postfixes = {}
        postfix, prefix = 0, 0
        minOperations = float("inf")

        for i in range(len(nums)-1, -1, -1):
            postfix += nums[i]
            postfixes[postfix] = arrayLength - i
            if postfix == x:
                minOperations = min(minOperations, arrayLength - i)

        if postfix < x:
            return -1
        if postfix == x:
            return arrayLength

        for i, num in enumerate(nums):
            target = x - prefix
            prefix += num
            if target in postfixes:
                minOperations = min(minOperations, i + postfixes[target])
            elif x == prefix:
                minOperations = min(minOperations, i + 1)
        return minOperations if minOperations != float("inf") else -1
        
